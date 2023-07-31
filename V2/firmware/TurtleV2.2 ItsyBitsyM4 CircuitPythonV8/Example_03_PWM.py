import board
import digitalio
import pwmio

print('Running "%s"' % __file__)

# define pins used
rightLEDPin = board.D7

# set the pin as a PWM output
rightLED = pwmio.PWMOut(rightLEDPin, frequency=5000, duty_cycle=0)


while True:
    for i in range(0, 65535, 10):
        rightLED.duty_cycle = i
    for i in range(65535, 0, -10):
        rightLED.duty_cycle = i

'''
* Explore:
    * We’ve started using a new python command called range,
      which generates a set of values for us one at a time.
      In the REPL console, try the following commands:
        for i in range(10): print(i)
        for i in range(5:10): print(i)
        for i in range(0, 10, 2): print(i)\
    * Can you make the LED fade quicker or slower?
    * Import the random module and use the random.randint()
      function to create a random flicker?
'''
