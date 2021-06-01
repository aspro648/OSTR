'''
Turtle Robot (V2.2) https://github.com/aspro648/OSTR/
@TheMakersBox
#TurtleRobot
648.ken@gmail.com

You have an Adafruit ItsyBitsy M4:
    https://learn.adafruit.com/introducing-adafruit-itsybitsy-m4
Running CiruitPython version 6.2.0
    https://circuitpython.org/board/itsybitsy_m4_express/
With libraries from adafruit-circuitpython-bundle-6.x-mpy-20210521.zip:
    https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases
Download Mu Editor at https://codewith.mu/en/download

Workshop Links:
  Handouts: https://github.com/aspro648/OSTR/raw/master/V2/docs/Robotics_Handouts.pdf
  Mechanical Assembly: https://github.com/aspro648/OSTR/raw/master/V2/docs/Mechanical_Assembly.pdf
  Name Plate Design: https://github.com/aspro648/OSTR/raw/master/V2/docs/Name_Plate_3D_Design.pdf

Activites:
  https://www.tinkercad.com/joinclass/6I6RPXA9QDII
  https://groklearning.com/hoc/activity/snowflake/

Turtle Name:  Turtle
Turtle Owner: Your Name
Serial Number: 015
'''

from turtle import *
from tone import tone         # tone(frequency, duration)
from RGBled import RGBled     # RGBled((red, blue, green))
myColor = (0, 0, 153)       #https://www.rapidtables.com/web/color/RGB_Color.html
RGBled(myColor, brightness=0.15)

print("Hello!  Edit 'code.py' to change the robots behavor.\n")

# Uncomment just code file below that you would like to execute and save this file.
# Click on [Serial] button to see code output.
# Open the individual ".py" file to see what it does or modify it.

# --- The following scripts are Turtle Robot specific ---
#import wheel_calibration
#import eye_check
#import example
#import music_example
#import turtle_obstacles

# --- The following will run on the Robot or on a laptop ---
#import turtle_snowflake_example1
#import turtle_snowflake_example2
#import turtle_mySnowflake
#import turtle_font_example
import turtle_cursive_example
#import turtle_goto_example
