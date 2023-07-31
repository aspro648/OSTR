import board
import digitalio
from time import sleep

print('Running "%s"' % __file__)

# define pins used
rightLEDPin = board.D7

rightLED = digitalio.DigitalInOut(rightLEDPin)

# assign pins as input or output
rightLED.direction = digitalio.Direction.OUTPUT

while True:
    rightLED.value = True
    sleep(0.5)
    rightLED.value = False
    sleep(0.5)

'''
Explore:
    * Before the “while True” loop, create a variable called “delay_time = 0.5” and substitute it in for the actual values in the time.sleep() functions.
    * The “time.sleep” command pauses execution for a specified number of seconds.
        - How quick can you make the delay and still see the blinking?
        - What if you move the board back and forth?
          (see https://en.wikipedia.org/wiki/Flicker_fusion_threshold )
    * If you remove the “while True:” statement what happens?
        - Indentation is used in Python to control program flow.
        - It helps with readability, but can also cause frustration.
    * There is a python module called random.  In REPL, try:
        import random
        random.random()
        - Can you use this function to create a random flicker?
    * Write the code to blink the other LED attached to board.D11.
    * There is a red LED onboard the Itsy Bitsy attached to board.D13.
      Can you make it blink?
    * There is also an onboard RGB LED that is set by importing Example_01_RGB.py
      in the code.py file.
        - Open the Example file and change the color.
        - What happens to the RGB LED when code execution is complete?

'''



