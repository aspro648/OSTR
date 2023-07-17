import board
import digitalio
import analogio
import time

# define pins used
green_led = digitalio.DigitalInOut(board.D2)
adc = analogio.AnalogIn(board.A0)

# assign pins as input or output
green_led.direction = digitalio.Direction.OUTPUT


while True:
    print(adc.value)
    if (adc.value / 65535) < 0.5:
        green_led.value = True
    else:
        green_led.value = False
    time.sleep(0.1) #  slow down a bit so we can read console
e
