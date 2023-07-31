import digitalio
import analogio
import settings
from time import sleep

print('Running "%s"' % __file__)
# This program is used to test the functionality of the LEDs,
# IR Emitter/Detector, and button.

# define pins used
buttonPin = settings.buttonPin
emitterPin = settings.emitterPin
rightLEDPin = settings.rightLEDPin
rightDetectorPin = settings.rightDetectorPin
leftLEDPin = settings.leftLEDPin
leftDetectorPin = settings.leftDetectorPin

# assign pins as input or output
button = digitalio.DigitalInOut(buttonPin)
emitter = digitalio.DigitalInOut(emitterPin)
rightLED = digitalio.DigitalInOut(rightLEDPin)
leftLED = digitalio.DigitalInOut(leftLEDPin)
rightDetector = analogio.AnalogIn(rightDetectorPin)
leftDetector = analogio.AnalogIn(leftDetectorPin)

# set direction
button.switch_to_input(pull=digitalio.Pull.UP)
emitter.direction = digitalio.Direction.OUTPUT
rightLED.direction = digitalio.Direction.OUTPUT
leftLED.direction = digitalio.Direction.OUTPUT

# turn on IR LED
emitter.value = True

while True:
    rightReading = rightDetector.value / 65535
    leftReading = leftDetector.value / 65535
    print("(%.2f, %.2f, %d)" % (rightReading, leftReading, button.value))
    if rightReading < 0.5 or not button.value:
        rightLED.value = True
    else:
        rightLED.value = False

    if leftReading < 0.5 or not button.value:
        leftLED.value = True
    else:
        leftLED.value = False

    sleep(0.1) #  slow down a bit so we can read console


