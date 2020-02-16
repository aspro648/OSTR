import board
import digitalio
import time
from analogio import AnalogIn
from turtle import *

# The LED will illuminate when an object is close enough to reflect IR back to the detector.
# With board attached to computer, lanuch plotter in Mu to see graphical response rates.

print('\nRunning "turtle_obsticles_complete.py"')

# Turn IR LEDs on.  You might be able to see them in a camera.
emitter.value = True
threshold = 0.8  #between 0 and 1.  Higher = more sensistive

while True:
    rightVal = rightDetector.value / 65535  # The analog value is 12-bits, thus 0 - 65535
    leftVal = leftDetector.value / 65535    # We convert it to a ratio to make it easier to read.

    if rightVal < threshold or leftVal < threshold:
        backward(1)
        if rightVal < threshold:
            rightLED.value = True
        if leftVal < threshold:
            leftLED.value = True
        if rightVal < threshold and threshold < threshold:
            left(90)
        elif rightVal < threshold:
            left(50)
        else:
            right(50)

    else:
        forward(1)
        rightLED.value = False  # Turn LED off
        leftLED.value = False