from turtle import *

'''
    Place turtle in center of paper facing east (right).
    Turtle will go forward 100mm, backwards 100mm, and then rotate right 360 degrees.
    Turtle will repeat this four times.

    The following parameters can be adjusted in settings.py:
    - If the length of the line is > 100mm, increase wheel_dia.
    - If the repeated lines rotate counter-clockwise, increase wheel_base.
    - If Turtle is moving backwards and turning left, change invert_direction in settings.py.
    - If the servo is not raising and lowering the pen correctly, adjust
      PEN_UP and PEN_DOWN angles.
'''

print('Running "%s"' % __file__)

for turns in range(4):
    pendown()
    forward(100)
    penup()
    backward(100)
    right(360)



