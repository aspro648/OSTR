#!/usr/bin/python
# turtle-hershey-example - a trivial demo to say hello
# scruss - 2014-05-06 - dual WTFPL (srsly)
# https://github.com/scruss/python-hershey
from PIL import Image
import io
from turtle import *
from tkinter import *  # Python 3
try:
    from lib.hersey_font import simple as glyphs
    #from lib.hersey_font import simple as glyphs
    #x_scale = 2.5
except ImportError:
    import sys
    print('\nError: Need file "lib/hersey_font.py"')
    sys.exit()

'''
Place turtle in center of paper facing east.

Hershey fonts were developed in the 1960s for rendering text on cathode ray tube displays.
They use a rather cryptic method of encoding coordinate pairs using ascii characters.
Since the turtle output is vector (direction and distance), Hershey font codes can be
converted to turtle code on the fly, giving us access to cursive turtle writing!

use either:
    from hersey_font import cursive as glyphs
    from hersey_font import simple as glyphs

'''

print('Example of using vector fonts from turtle_cursive_example.py')

# Additional fonts in '/lib/hersey_codes.txt'.
# Save them in glyph dictionary in '/lib/hersey_font.py'.

speed(0)


def char2val(c):  # data is stored as signed bytes relative to ASCII R
    return ord(c) - ord('R')


def hersheyparse(dat):
    """ reads a line of Hershey font text """
    print(dat)
    print(dat[3:6])
    if int(dat[3:6]) - 1 < 2:  # fail if there impossibly few vertices
        return None
    lines = []
    for s in dat[8:].split(' R'):
        line = []
        i = 0
        temp = list(s)
        while i < len(temp):
            line.append((char2val(s[i]), char2val(s[i+1])))
            i = i + 2

        # print('line = %s' % line)
        lines.append(line)
    glyph = {  # character code in columns 1-6; it's not ASCII
               # indicative number of vertices in columns 6-9
               # left side bearing encoded in column 9
               # right side bearing encoded in column 10
        'charcode': int(dat[0:3]),
        'vertices': int(dat[3:6]) - 1,
        'left': char2val(dat[6]),
        'right': char2val(dat[7]),
        'lines': lines,
        }
    return glyph

# speed(1)
paper_x = 280
paper_y = 218
penup()
goto(paper_x, paper_y)
pendown()
goto(-paper_x, paper_y)
goto(-paper_x, -paper_y)
goto(paper_x, -paper_y)
goto(paper_x, paper_y)
penup()

x_scale = 1.8
y_scale = -x_scale  # remember: Y is +ve *down* for Hershey ...

penup()
pensize(5)

def word(letters):
    global x, y
    for c in list(letters):
        vals = glyphs.get(c)
        if vals:
            glyph = hersheyparse(glyphs[c])
            print(glyph)
            x_origin = x
            y_origin = y
            for line in glyph['lines']:
                first = 1
                for pt in line:
                    if first == 1:
                        first = 0
                        goto(x_origin + x_scale * (pt[0] - glyph['left']),
                             y_origin + y_scale * pt[1])
                        pendown()
                    else:
                        goto(x_origin + x_scale * (pt[0] - glyph['left']),
                             y_origin + y_scale * pt[1])
                penup()

                # don't forget to move to (right sidebearing, 0) at end of draw
                x = x_origin + x_scale * (glyph['right'] - glyph['left'])
                y = y_origin
        else:
            print("No glyph found for '%s'." % c)
    penup()

pencolor('green')
x = -120   # start turtle in middle, move to edge
y = 25
word("Turtle")
x = -120   # start turtle in middle, move to edge
y = -25
word("Robot")

scale = 2.5
pointsfull = [(0.0, 0.0), (-12.0, -12.0), (-36.0, -6.0), (-54.0, -24.0),
          (-42.0, -42.0), (-48.0, -54.0), (-66.0, -36.0), (-90.0, -42.0),
          (-114.0, -30.0), (-132.0, -48.0), (-144.0, -36.0), (-126.0, -24.0),
          (-138.0, 0.0), (-126.0, 24.0), (-144.0, 36.0), (-132.0, 48.0),
          (-114.0, 30.0), (-90.0, 42.0), (-66.0, 36.0), (-48.0, 54.0),
          (-42.0, 42.0), (-54.0, 24.0), (-36.0, 6.0), (-12.0, 12.0),
          (0.0, 0.0)]

points = [(0.0, 0.0), (-12.0, -12.0), (-36.0, -6.0), (-54.0, -24.0),
          (-42.0, -42.0), (-48.0, -54.0), (-66.0, -36.0), (-90.0, -42.0),
          (-114.0, -30.0), (-132.0, -48.0), (-144.0, -36.0), (-126.0, -24.0),
          (-138.0, 0.0)]

points_shell = [(-30.0, 0),(-66.0, -36.0), (-90.0, -42.0),
          (-114.0, -30.0), (-126.0, -24.0),
          (-138.0, 0.0)]

xoffset = 180
yoffset = 0


pencolor('lightgreen')
penup()
goto(points_shell[0][0] * scale + xoffset,
     points_shell[0][1] * scale + yoffset)
pendown()
for point in points_shell:
    x, y = point
    goto(x * scale + xoffset, y * scale + yoffset)
for point in reversed(points_shell):
    x, y = point
    goto(x * scale + xoffset, -y * scale + yoffset)

penup()
goto(xoffset, yoffset)
pendown()

for point in points:
    x, y = point
    goto(x * scale + xoffset, y * scale + yoffset)
for point in reversed(points):
    x, y = point
    goto(x * scale + xoffset, -y * scale + yoffset)

'''
scale = 1.65
xoffset = 87
for point in points:
    x, y = point
    goto(x * scale + xoffset, y * scale + yoffset)
'''

penup()
setheading(90) #North
forward(400)
done()

ts = getscreen()
ts.getcanvas().postscript(file="duck.eps")
im = Image.open(io.BytesIO(ps.encode("utf-8")))
im.save("test.png", format="PNG")

