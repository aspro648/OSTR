import digitalio
import analogio
import settings
from time import sleep

print('Running "%s"' % __file__)

# define pins used
emitterPin = settings.emitterPin
rightLEDPin = settings.rightLEDPin
rightDetectorPin = settings.rightDetectorPin

# assign pins as input or output
emitter = digitalio.DigitalInOut(emitterPin)
rightLED = digitalio.DigitalInOut(rightLEDPin)
rightDetector = analogio.AnalogIn(rightDetectorPin)

# set direction
emitter.direction = digitalio.Direction.OUTPUT
rightLED.direction = digitalio.Direction.OUTPUT

# turn on IR LED
emitter.value = True

while True:
    reading = rightDetector.value / 65535
    print("(%.2f)" % reading)
    if reading < 0.5:
        rightLED.value = True
    else:
        rightLED.value = False
    sleep(0.1) #  slow down a bit so we can read console

'''
Explore:
    * At what distance from an object does the visible LED light?
    * We are printing the fraction of full scale so it can be graphed:
        - Click [Plotter] button and see output.
    * Does the distance vary between objects like your hand versus a cell phone?
    * With no object present, the reading is still less than the full 16-bit value of 65535.
      Why?  What can you do to improve it?
    * What would happen if we try to read the IR detector as a digital input instead of analog?
        - Would there be an advantage to using digital input instead of analog?
'''
