#https://microcontrollerslab.com/28byj-48-stepper-motor-raspberry-pi-pico-micropython/

import digitalio
import board
from time import sleep


# stepper wires [blue->pink->yel->org]
In1 = digitalio.DigitalInOut(board.D13)
In2 = digitalio.DigitalInOut(board.D12)
In3 = digitalio.DigitalInOut(board.D11)
In4 = digitalio.DigitalInOut(board.D10)

# assign pins as input or output
In1.direction = digitalio.Direction.OUTPUT
In2.direction = digitalio.Direction.OUTPUT
In3.direction = digitalio.Direction.OUTPUT
In4.direction = digitalio.Direction.OUTPUT

# put connections in List to make life easier
pins = [In1, In2, In3, In4]

patterns = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1]]

DELAY = 0.001
STEPS = 513  # this is a full 360º

for step in range(STEPS):
    for pattern in reversed(patterns):
        for i in range(len(pins)):
            pins[i].value = pattern[i]
            sleep(DELAY)

