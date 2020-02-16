import board
import digitalio
from time import sleep
from analogio import AnalogIn

# The LED will indicate when an object is close enough to reflect IR back to the detector.
# With board attached to computer, lanuch plotter in Mu to see graphical response rates.

print('\nRunning "turtle_eye_check.py"')
print('Click on the [Plotter] button to see a graph of the output.')
print('Turtle robot shield must be attached.')
print('What happens when you hold your hand in front of the clear LED?')

# Turn IR LEDs on.  You might be able to see them in a camera.
emitter.value = True

for x in range(3):
    rightLED.value = True
    leftLED.value = True
    sleep(0.25)
    rightLED.value = False
    leftLED.value = False
    sleep(0.25)

while True:
    rightVal = rightDetector.value / 65535  # The analog value is 12-bits, thus 0 - 65535
    leftVal = leftDetector.value / 65535    # We convert it to a ratio to make it easier to read.
    if rightVal > 0.5:
        rightLED.value = False  # Turn LED off
    else:
        rightLED.value = True   # Or turn in on.
    if leftVal > 0.5:
        leftLED.value = False
    else:
        leftLED.value = True
    isButtonPushed = not button.value #pulled up (True) when not pushed
    print('(%.2f, %.2f, %d)' % (leftVal, rightVal, isButtonPushed))  # Formats output to two decimal places
    sleep(0.1)  # Don't go too fast if we're trying to read the output!