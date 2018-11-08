# Learn more about CircuitPython at
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials

import time
import board
 
# ItsyBitsy M0 Express has a built in RGB LED
import adafruit_dotstar
led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)

print('"Running blink.py"')

# How would you control the brightness of an LED?
led.brightness = 0.3
# Try shaking it back and forth to see.


while True:
    print("red")
    led[0] = (255, 0, 0)
    time.sleep(1)
    print("green")
    led[0] = (0, 255, 0)
    time.sleep(1)
    print("blue")
    led[0] = (0, 0, 255)
    time.sleep(1)