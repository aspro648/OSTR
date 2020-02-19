import board
import digitalio
from time import sleep
import adafruit_dotstar


led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)


def RGBled(color, brightness=1):
    led[0] = color
    led.brightness = brightness


RGBled((94, 40, 62)) #ChickTECH pink!

