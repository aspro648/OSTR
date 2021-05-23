from turtle import *

'''
Learn how to make a snowflake at
https://studio.code.org/s/frozen/stage/1/puzzle/12

This code will run on the Turtle Robot or on a laptop.
Pensize() & color() are not implemented in robot, but will
not cause an error.

Can you use the random.randrange(low, high) to create
a variable number of arms or lengths?
'''

print('Running "turtle_snowflake_example2.py"')

pensize(5)          # pensize & color are not implemented in robot
pencolor('skyblue')

arms = 5
length = 50
angle = 60

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

penup()
setheading(90)  # North
forward(100)
done()  # this releases the motors to save power
