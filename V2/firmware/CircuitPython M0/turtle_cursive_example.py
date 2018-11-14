#!/usr/bin/python
# turtle-hershey-example - a trivial demo to say hello
# scruss - 2014-05-06 - dual WTFPL (srsly)
# https://github.com/scruss/python-hershey

from turtle import *
import math


'''
Hershey fonts were developed in the 1960s for rendering text on cathode ray tube displays.
They use a rather cryptic method of encoding coordinate pairs using ascii characters.
Since the turtle output is vector (direction and distance), Hershey font codes can be
converted to turtle code on the fly, giving us access to cursive turtle writing!

'''

# A dictionary for the letters we're going to use. 
# This is memory intensive, so only add what you need from 'hersey_codes.txt':
glyphs = {
    'h': '  658 29M\MVOSRNSLTITGSFQGPIOMNSM[ RM[NXOVQSSRURVSVUUXUZV[W[YZZY\V',
    'e': '  655 17NXOYQXRWSUSSRRQROSNUNXOZQ[S[UZVYXV',
    'l': '  662 18OWOVQSTNULVIVGUFSGRIQMPTPZQ[R[TZUYWV',
    'o': '  665 23LZRRPRNSMTLVLXMZO[Q[SZTYUWUUTSRRQSQURWTXWXYWZV',
    }


letters = 'hello'


def char2val(c):  # data is stored as signed bytes relative to ASCII R
    return ord(c) - ord('R')


def hersheyparse(dat):
    """ reads a line of Hershey font text """

    if int(dat[5:8]) - 1 < 2:  # fail if there impossibly few vertices
        return None
    lines = []
    for s in dat[10:].split(' R'):
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
        'charcode': int(dat[0:5]),
        'vertices': int(dat[5:8]) - 1,
        'left': char2val(dat[8]),
        'right': char2val(dat[9]),
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
    glyph = hersheyparse(glyphs[c])
    #print(glyph)
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

penup()
done()