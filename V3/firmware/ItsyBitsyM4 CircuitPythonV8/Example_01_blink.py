import board
import digitalio
from time import sleep

print("Running Example_01_blink.py")

# define pins used
green_led = digitalio.DigitalInOut(board.D2)

# assign pins as input or output
green_led.direction = digitalio.Direction.OUTPUT

while True:
    green_led.value = True
    sleep(0.5)
    green_led.value = False
    sleep(0.5)





