#!/usr/bin/python
# turtle-hershey-example - a trivial demo to say hello
# scruss - 2014-05-06 - dual WTFPL (srsly)
# https://github.com/scruss/python-hershey

import turtle

letters = 'TURTLE'

def char2val(c):  # data is stored as signed bytes relative to ASCII R
    return ord(c) - ord('R')


def hersheyparse(dat):
    """ reads a line of Hershey font text """

    if int(dat[5:8]) - 1 < 2:  # fail if there impossibly few vertices
        return None
    lines = []
    # individual lines are stored separated by <space>+R
    # starting at col 11
    #for s in split(dat[10:], ' R'):
    for s in dat[10:].split(' R'):
        print('s= %s' %s)
        # each line is a list of pairs of coordinates
        # NB: origin is at centre(ish) of character
        #     Y coordinates **increase** downwards

        #line = map(None, *[iter(map(char2val, list(s)))] * 2)
        line = []
        i = 0
        temp = list(s)
        while i < len(temp):
            line.append((char2val(s[i]), char2val(s[i+1])))
            i = i + 2          

        print('line = %s' % line)
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


# a hash for the four chars we're going to use: they're cursive

glyphs = {
    'A': '    1  9MWRMNV RRMVV RPSTS',
    'B': '    2 16MWOMOV ROMSMUNUPSQ ROQSQURUUSVOV',
    'C': '    3 11MXVNTMRMPNOPOSPURVTVVU',
    'D': '    4 12MWOMOV ROMRMTNUPUSTURVOV',
    'E': '    5 12MWOMOV ROMUM ROQSQ ROVUV',
    'F': '    6  9MVOMOV ROMUM ROQSQ',
    'G': '    7 15MXVNTMRMPNOPOSPURVTVVUVR RSRVR',
    'H': '    8  9MWOMOV RUMUV ROQUQ',
    'I': '    9  3PTRMRV',
    'J': '   10  7NUSMSTRVPVOTOS',
    'K': '   11  9MWOMOV RUMOS RQQUV',
    'L': '   12  6MVOMOV ROVUV',
    'M': '   13 12LXNMNV RNMRV RVMRV RVMVV',
    'N': '   14  9MWOMOV ROMUV RUMUV',
    'O': '   15 14MXRMPNOPOSPURVSVUUVSVPUNSMRM',
    'P': '   16 10MWOMOV ROMSMUNUQSROR',
    'Q': '   17 17MXRMPNOPOSPURVSVUUVSVPUNSMRM RSTVW',
    'R': '   18 13MWOMOV ROMSMUNUQSROR RRRUV',
    'S': '   19 13MWUNSMQMONOOPPTRUSUUSVQVOU',
    'T': '   20  6MWRMRV RNMVM',
    'U': '   21  9MXOMOSPURVSVUUVSVM',
    'V': '   22  6MWNMRV RVMRV',
    'W': '   23 12LXNMPV RRMPV RRMTV RVMTV',
    'X': '   24  6MWOMUV RUMOV',
    'Y': '   25  7MWNMRQRV RVMRQ',
    'Z': '   26  9MWUMOV ROMUM ROVUV',
    '0': '  200 12MWRMPNOPOSPURVTUUSUPTNRM',
    '1': '  201  4MWPORMRV',
    '2': '  202  9MWONQMSMUNUPTROVUV',
    '3': '  203 15MWONQMSMUNUPSQ RRQSQURUUSVQVOU',
    '4': '  204  7MWSMSV RSMNSVS',
    '5': '  205 14MWPMOQQPRPTQUSTURVQVOU RPMTM',
    '6': '  206 14MWTMRMPNOPOSPURVTUUSTQRPPQOS',
    '7': '  207  6MWUMQV ROMUM',
    '8': '  208 19MWQMONOPQQSQUPUNSMQM RQQOROUQVSVUUURSQ',
    '9': '  209 14MWUPTRRSPROPPNRMTNUPUSTURVPV',
    '.': '  210  6PURURVSVSURU',
    ',': '  211  7PUSVRVRUSUSWRY',
    ':': '  212 12PURPRQSQSPRP RRURVSVSURU',
    ';': '  213 13PURPRQSQSPRP RSVRVRUSUSWRY',
    '!': '  214 12PURMRR RSMSR RRURVSVSURU',
    '?': '  215 17NWPNRMSMUNUPRQRRSRSQUP RRURVSVSURU',
    'h': '  658 29M\MVOSRNSLTITGSFQGPIOMNSM[ RM[NXOVQSSRURVSVUUXUZV[W[YZZY\V',
    'e': '  655 17NXOYQXRWSUSSRRQROSNUNXOZQ[S[UZVYXV',
    'l': '  662 18OWOVQSTNULVIVGUFSGRIQMPTPZQ[R[TZUYWV',
    'o': '  665 23LZRRPRNSMTLVLXMZO[Q[SZTYUWUUTSRRQSQURWTXWXYWZV',
    }

x_scale = 3
y_scale = -3  # remember: Y is +ve *down* for Hershey ...
x = 0
y = 0
turtle.penup()
turtle.pensize(3)
turtle.goto(x, y)
for c in list(letters):
    glyph = hersheyparse(glyphs[c])
    print(glyph)
    x_origin = x
    y_origin = y
    for line in glyph['lines']:
        first = 1
        for pt in line:
            if first == 1:
                first = 0
                turtle.goto(x_origin + x_scale * (pt[0] - glyph['left'
                            ]), y_origin + y_scale * pt[1])
                turtle.pendown()
            else:
                turtle.goto(x_origin + x_scale * (pt[0] - glyph['left'
                            ]), y_origin + y_scale * pt[1])
        turtle.penup()

        # don't forget to move to (right sidebearing, 0) at end of draw

        x = x_origin + x_scale * (glyph['right'] - glyph['left'])
        y = y_origin

turtle.done()
