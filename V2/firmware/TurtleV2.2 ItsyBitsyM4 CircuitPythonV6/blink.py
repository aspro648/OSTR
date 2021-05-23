# Learn more about CircuitPython at
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials

import time
import board
import digitalio
from RGBled import RGBled

print('"Running blink.py"')

'''
# ItsyBitsy Express has a built in RGB LED
import adafruit_dotstar
try:
    RGBled = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
except ValueError:
    print("Already implement APA102_MOSI")
'''

# And a red LED hooked to pin D13
red_led = digitalio.DigitalInOut(board.D13)
red_led.direction = digitalio.Direction.OUTPUT
red_led.value = True

# How would you control the brightness of an LED?
RGBled.led.brightness = 0.3
# Try shaking it back and forth to see.

# Colors are repesented by the three values (0 - 255) for (red, green, blue)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)

# Find your favorite color RGB values at https://www.rapidtables.com/web/color/RGB_Color.html
# and try it.
myColor = (255, 255, 255)  # What color do you think this is?

# Add a variable 'delayTime' so you can change the speed in one place.
# Is there a way to generate random numbers?

while True:
    print("I'm red")
    RGBled[0] = red
    time.sleep(2)
    print("I'm green")
    RGBled[0] = green
    time.sleep(2)
    print("I'm blue")
    RGBled[0] = blue
    time.sleep(2)
    red_led.value = not red_led.value # toggle red LED
