# https://eecs.wsu.edu/~schneidj/PyBook/chap13.pdf
# https://en.wikipedia.org/wiki/Koch_snowflake

from turtle import *

penup()
backward(50)
left(90)
backward(35)
right(90)


def ks(length, d):
    if d == 0:
        forward(length)
    else:
        length = length / 3
        d = d - 1
        ks(length, d)
        right(60)
        ks(length, d)
        left(120)
        ks(length, d)
        right(60)
        ks(length, d)

itterations = 2 #0 through ...

pendown()

for i in range(3):
    ks(125, itterations)
    left(120)

penup()
backward(50)
