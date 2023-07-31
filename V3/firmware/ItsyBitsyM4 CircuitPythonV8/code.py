'''
Turtle Robot (V3.0) https://github.com/aspro648/OSTR/
@TheMakersBox
#TurtleRobot
648.ken@gmail.com

You have an Adafruit ItsyBitsy M4:
    https://learn.adafruit.com/introducing-adafruit-itsybitsy-m4
Running CiruitPython version 8.2.0
    https://circuitpython.org/board/itsybitsy_m4_express/
With libraries from adafruit-circuitpython-bundle-8.x-mpy-20230709:
    https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases
Download Mu Editor at https://codewith.mu/en/download

Workshop Links:
  Handouts: https://github.com/aspro648/OSTR/raw/master/V2/docs/Robotics_Handouts.pdf
  Mechanical Assembly: https://github.com/aspro648/OSTR/raw/master/V2/docs/Mechanical_Assembly.pdf


Activites:
  https://www.tinkercad.com/joinclass/6I6RPXA9QDII
  https://groklearning.com/hoc/activity/snowflake/
'''


from tone import tone         # tone(frequency, duration)
from RGBled import RGBled     # RGBled((red, blue, green))
myColor = (0, 0, 255)         # https://www.rapidtables.com/web/color/RGB_Color.html
RGBled(myColor, brightness=0.15)

print("Hello!  Edit 'code.py' to change the robots behavor.\n")

# Uncomment just code file below that you would like to execute and save this file.
# Click on [Serial] button to see code output.
# Open the individual ".py" file to see what it does or modify it.

# --- The following will run on the Robot or on a laptop ---
#import turtle_wheel_calibration
#import turtle_snowflake_example1
#import turtle_snowflake_example2
#import turtle_mySnowflake
#import turtle_font_example
#import turtle_cursive_example
#import turtle_goto_example

# --- The following scripts are Turtle Robot specific ---
import eye_check
#import Example_01_blink
#import Example_01_blink_RGB
#import Example_02_button
#import Example_03_PWM
