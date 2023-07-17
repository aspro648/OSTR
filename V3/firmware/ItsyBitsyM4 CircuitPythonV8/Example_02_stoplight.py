

import board
import digitalio
from time import sleep
from time import monotonic as now


print("Running Example_01_blink.py")

# define pins used
green_led = digitalio.DigitalInOut(board.D2)
yellow_led = digitalio.DigitalInOut(board.A3)
red_led = digitalio.DigitalInOut(board.A4)
button = digitalio.DigitalInOut(board.MISO)

# assign pins as input or output
green_led.direction = digitalio.Direction.OUTPUT
yellow_led.direction = digitalio.Direction.OUTPUT
red_led.direction = digitalio.Direction.OUTPUT
button.switch_to_input(pull=digitalio.Pull.UP)


while True:
    red_led.value = False
    green_led.value = True
    wait_time = now() + 10
    while(button.value and now() < wait_time):
        pass
    print("signal recieved")
    green_led.value = False
    yellow_led.value = True
    sleep(3)
    yellow_led.value = False
    red_led.value = True
    sleep(6)





