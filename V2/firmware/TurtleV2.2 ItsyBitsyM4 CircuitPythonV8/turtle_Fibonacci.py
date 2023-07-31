# https://www.codheadz.com/2019/06/30/Trees-with-Turtle-in-Python/


from turtle import *

print('Running "%s"' % __file__)

penup()
setheading(90)
backward(75)
pendown()

def draw_branch(len):
    angle = 25
    if (len > 5):
        forward(len)
        right(angle)
        draw_branch(len - 5)
        left(angle * 2)
        draw_branch(len - 5)
        right(angle)
        backward(len)

draw_branch(35)

