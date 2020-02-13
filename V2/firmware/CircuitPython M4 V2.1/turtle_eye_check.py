import board
import digitalio
import time
from analogio import AnalogIn

# The LED will illuminate when an object is close enough to reflect IR back to the detector.
# With board attached to computer, lanuch plotter in Mu to see graphical response rates.

print('\nRunning "turtle_eye_check.py"')
print('Click on the [Plotter] button to see a graph of the output.')
print('Turtle robot shield must be attached.')
print('What happens when you hold your hand in front of the clear LED?')
time.sleep(5)
# Pin assignments
leftEmitter = digitalio.DigitalInOut(board.D10)
leftLED = digitalio.DigitalInOut(board.D7)
rightEmitter = digitalio.DigitalInOut(board.D13)
rightLED = digitalio.DigitalInOut(board.D11)
button = digitalio.DigitalInOut(board.D12)
rightDetector = AnalogIn(board.A0)
leftDetector = AnalogIn(board.A1)

# Port setup
leftLED.direction = digitalio.Direction.OUTPUT
leftEmitter.direction = digitalio.Direction.OUTPUT
rightLED.direction = digitalio.Direction.OUTPUT
rightEmitter.direction = digitalio.Direction.OUTPUT
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Turn IR LEDs on.  You might be able to see them in a camera.
rightEmitter.value = True
leftEmitter.value = True


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
    print('(%.2f, %.2f)' % (leftVal, rightVal))  # Formats output to two decimal places
    time.sleep(0.1)  # Don't go too fast if we're trying to read the output!