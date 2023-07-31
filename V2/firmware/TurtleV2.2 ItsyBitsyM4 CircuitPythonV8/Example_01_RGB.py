import board
import digitalio
from time import sleep
import adafruit_dotstar


print('Running "%s" to set RGB LED color!' % __file__)

led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)

red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)

myColor = blue         # https://www.rapidtables.com/web/color/RGB_Color.html


def RGBled(color, brightness=1):
    led[0] = color
    led.brightness = brightness


RGBled(myColor, brightness=0.15)


if __name__ == '__main__':
    RGBled((94, 40, 62)) #ChickTECH pink!
    # Colors are repesented by the three values (0 - 255) for (red, green, blue)


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

