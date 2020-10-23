import board
import digitalio
import time
from analogio import AnalogIn
from turtle import *

# The LED will illuminate when an object is close enough to reflect IR back to the detector.
# With board attached to computer, lanuch plotter in Mu to see graphical response rates.

print('\nRunning "turtle_obstacles.py"')

# Turn IR LEDs on.  You might be able to see them in a camera.
emitter.value = True

threshold = 0.8  #between 0 and 1.  Higher = more sensistive

UP = True     # some alias to help track pen position
DOWN = False
penState = UP
penup()

while True:
    rightVal = rightDetector.value / 65535  # The analog value is 12-bits, thus 0 - 65535
    leftVal = leftDetector.value / 65535    # We convert it to a ratio to make it easier to read.

    # Check IR values and turn on LED if obstacle detected
    if rightVal < threshold or leftVal < threshold:
        if rightVal < threshold:
            rightLED.value = True
        if leftVal < threshold:
            leftLED.value = True

        # what kind of logic can you add here to help the turtle avoid the obstacle?

    else:  #go ahead an move
        forward(1)
        rightLED.value = False  # Turn LED off
        leftLED.value = False

    if (isButtonPushed()):
        while(isButtonPushed()):
            time.sleep(0.1)
        penState = not(penState)
        if penState:
            penup()
        else:
            pendown()

    #print('(%.2f, %.2f, %d)' % (leftVal, rightVal, penState))  # Formats output to two decimal places
    #time.sleep(0.1)
