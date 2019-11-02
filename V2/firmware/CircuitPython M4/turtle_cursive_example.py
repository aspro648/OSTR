#!/usr/bin/python
# turtle-hershey-example - a trivial demo to say hello
# scruss - 2014-05-06 - dual WTFPL (srsly)
# https://github.com/scruss/python-hershey

from turtle import *
import math
from hersey_font import cursive as glyphs


'''
Hershey fonts were developed in the 1960s for rendering text on cathode ray tube displays.
They use a rather cryptic method of encoding coordinate pairs using ascii characters.
Since the turtle output is vector (direction and distance), Hershey font codes can be
converted to turtle code on the fly, giving us access to cursive turtle writing!

use either:
    from hersey_font import cursive as glyphs
    from hersey_font import simple as glyphs

'''

print('Example of using vector fonts from turtle_cursivee_example.py')

# Additional fonts in 'hersey_codes.txt'.
# Save them in glyph dictionary in 'hersey_script.py'.


letters = "Hello"


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

        #print('line = %s' % line)
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

#speed(1)
x_scale = 3
y_scale = -x_scale  # remember: Y is +ve *down* for Hershey ...
x = 0
y = 0
penup()
pensize(3)

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
                    goto(x_origin + x_scale * (pt[0] - glyph['left'
                                ]), y_origin + y_scale * pt[1])
                    pendown()
                else:
                    goto(x_origin + x_scale * (pt[0] - glyph['left'
                                ]), y_origin + y_scale * pt[1])
            penup()

            # don't forget to move to (right sidebearing, 0) at end of draw
            x = x_origin + x_scale * (glyph['right'] - glyph['left'])
            y = y_origin
    else:
        print("No glyph found for '%s'." % c)
penup()
done()
