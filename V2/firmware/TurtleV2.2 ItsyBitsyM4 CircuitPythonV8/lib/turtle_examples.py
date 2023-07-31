from turtle import *
import random
from lib.hersey_font import cursive as glyphs


def cursive(letters):

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
    y_scale = -x_scale  # remember: Y is +ve *down* for Hershey ...
    x = -100   # start turtle in middle, move to edge
    y = 0
    penup()
    pensize(3)
    backward(75)

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

    done()


def snowflake1(arms=6, length=30):

    print("snowflake1(arms=%s, length=%s)" % (arms, length))

    def draw(length):
      # this is a simple flunction to draw forward, lift pen, move backward
      pendown()
      forward(length)
      penup()
      backward(length)


    for arm in range(arms):
      pendown()
      forward(length * 1.5)
      right(45)
      draw(length)
      left(90)
      pendown()
      draw(length)
      right(45)
      backward(length * 1.5)
      left(360 / arms)

    penup()
    done()  # this releases the motors to save power


def snowflake2(arms=6, length=30, angle=60):

    print("snowflake1(arms=%s, length=%s, angle=%s)" % (arms, length, angle))
    pendown()
    for arm in range(arms):
        forward(length)
        right(angle)
        forward(length)
        left(angle)
        backward(length)
        right(angle)
        backward(length)
        right(360 / arms - angle)

    done()  # this releases the motors to save power


if __name__ == '__main__':
    snowflake1(arms=5)
    forward(200)
    snowflake2()
    forward(200)
    cursive("hello")
