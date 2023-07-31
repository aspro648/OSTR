#https://microcontrollerslab.com/28byj-48-stepper-motor-raspberry-pi-pico-micropython/

import digitalio
import settings
from time import sleep

print('Running "%s"' % __file__)

# Right stepper wires [blue->pink->yel->org]
In1 = digitalio.DigitalInOut(settings.R_In1_Pin)
In2 = digitalio.DigitalInOut(settings.R_In2_Pin)
In3 = digitalio.DigitalInOut(settings.R_In3_Pin)
In4 = digitalio.DigitalInOut(settings.R_In4_Pin)

# assign pins as input or output
In1.direction = digitalio.Direction.OUTPUT
In2.direction = digitalio.Direction.OUTPUT
In3.direction = digitalio.Direction.OUTPUT
In4.direction = digitalio.Direction.OUTPUT

# put connections in List to make life easier
pins = [In1, In2, In3, In4]

patterns = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1]]

for step in range(settings.steps_rev):
    for pattern in reversed(patterns):
        for i in range(len(pins)):
            pins[i].value = pattern[i]
            sleep(settings.delay_time / 1000)

'''
Explore:
    * How would you make the stepper turn in the opposite direction?
        - There are several suitable methods. Google “python reverse list”.
    * If your stepper has a wheel on it, how would you make it travel a set distance?
    * If your robot has steppers on both sides, what happens to the robot if both steppers rotate in the same direction?
    * How would you make your robot turn in a full revolution?
    * How would you make your robot turn a set number of degrees?
    * The settings.delay_time variable controls the speed.
        - How fast and slow can you go?
    * The [patterns] we used is called a Full Step, or Power Step Sequence.
        - Are there other sequences that would work?
        - What advantages or disadvantages do they have?
'''
