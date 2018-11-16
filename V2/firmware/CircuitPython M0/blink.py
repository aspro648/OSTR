# Learn more about CircuitPython at
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials

import time
import board
import digitalio

print('"Running blink.py"')
 
# ItsyBitsy M0 Express has a built in RGB LED
import adafruit_dotstar
led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)

# And a red LED hooked to pin D13
red_led = digitalio.DigitalInOut(board.D13)
red_led.direction = digitalio.Direction.OUTPUT
red_led.value = True

# How would you control the brightness of an LED?
led.brightness = 0.3
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
    led[0] = red
    time.sleep(1)
    print("I'm green")
    led[0] = green
    time.sleep(1)
    print("I'm blue")
    led[0] = blue
    time.sleep(1)
    red_led.value = not red_led.value # toggle red LED
    