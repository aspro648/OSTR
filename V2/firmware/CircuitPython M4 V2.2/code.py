'''
Turtle Robot (V2.1) design files and details at
https://github.com/aspro648/OSTR/
648.ken@gmail.com

You have an Adafruit ItsyBitsy M4:
    https://learn.adafruit.com/introducing-adafruit-itsybitsy-m4
Running CiruitPython version 4.1.0
    https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials
Download Mu Editor at https://codewith.mu/en/download

Workshop Links:
  https://www.tinkercad.com/joinclass/6I6RPXA9QDII
  https://groklearning.com/hoc/activity/snowflake/
  https://studio.code.org/s/frozen/stage/1/puzzle/1

Turtle Name:  Turtle
Turtle Owner: Your Name
'''

# Uncomment just code file below that you would like to execute and save this file.
# Click on [Serial] button to see code output.
# Open the individual ".py" file to see what it does or modify it.

print("Hello!  Edit 'code.py' to change the robots behavor.\n")

from tone import tone         # tone(frequency, duration)
from RGBled import RGBled     # RGBled((red, blue, green))
ChickTECH_pink = (94, 40, 62) #https://www.rapidtables.com/web/color/RGB_Color.html
RGBled(ChickTECH_pink)

# --- The following scripts are Turtle Robot specific ---
import turtle_wheel_calibration
#import turtle_eye_check
#import blink
#import rtttl_example
#import music_example
#import turtle_obstacles

# --- The following will run on the Robot or on a laptop ---
#import turtle_snowflake_example
#import mySnowflake
#import turtle_font_example
#import turtle_cursive_example
#import turtle_goto_example