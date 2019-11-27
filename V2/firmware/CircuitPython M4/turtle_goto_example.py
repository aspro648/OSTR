from turtle import *

print('Example of using goto(x, y) from turtle_goto.py')

# These are the points used for generating the "turtle" icon
# from \Lib\lib-tk\turtle.py, scaled and shifted

points = [(0, 0), (-8, -8), (-4, -24), (-16, -36), (-28, -28), (-36, -32), (-24, -44),
          (-28, -60), (-20, -76), (-32, -88), (-24, -96), (-16, -84), (0, -92),
          (16, -84), (24, -96), (32, -88), (20, -76), (28, -60), (24, -44), (36, -32),
          (28, -28), (16, -36), (4, -24), (8, -8), (0, 0)]

for point in points:
    x, y = point
    print("goto(%s, %s)" % (x,y))
    goto(x, y)

done()


