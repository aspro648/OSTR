from turtle import *

'''
Place turtle in center of paper facing east.

This code will run on the Turtle Robot or on a laptop.
Pensize() & color() are not implemented in robot, but will
not cause an error.
'''

print('Example of using goto(x, y) from turtle_goto.py')

# These are the points used for generating the "turtle" icon
# from \Lib\lib-tk\turtle.py, scaled and shifted

points = [(0.0, 0.0), (-12.0, -12.0), (-36.0, -6.0), (-54.0, -24.0),
          (-42.0, -42.0), (-48.0, -54.0), (-66.0, -36.0), (-90.0, -42.0),
          (-114.0, -30.0), (-132.0, -48.0), (-144.0, -36.0), (-126.0, -24.0),
          (-138.0, 0.0), (-126.0, 24.0), (-144.0, 36.0), (-132.0, 48.0),
          (-114.0, 30.0), (-90.0, 42.0), (-66.0, 36.0), (-48.0, 54.0), (-42.0, 42.0),
          (-54.0, 24.0), (-36.0, 6.0), (-12.0, 12.0), (0.0, 0.0)]

xoffset = 75
yoffset = 0

penup()
goto(xoffset, yoffset)
pendown()

for point in points:
    x, y = point
    goto(x + xoffset, y + yoffset)

penup()
goto(xoffset, 100)
done()
