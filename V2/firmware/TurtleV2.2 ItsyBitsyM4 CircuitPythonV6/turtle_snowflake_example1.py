from turtle import *
import random

'''
Learn how to make a snowflake at
https://groklearning.com/hoc/activity/snowflake/

This code will run on the Turtle Robot or on a laptop.
Pensize() & color() are not implemented in robot, but will
not cause an error.

Can you use the random.randrange(low, high) to create
a variable number of arms or lengths?
'''

print('Running "turtle_snowflake_example1.py"')
pensize(5)          # pensize & color are not implemented in robot
pencolor('skyblue')

number_of_arms = 6  # Change this variable to add arms
length = 30         # Change is variable to change snowflake size


def draw(length):
  # this is a simple flunction to draw forward, lift pen, move backward
  pendown()
  forward(length)
  penup()
  backward(length)


for arm in range(number_of_arms):
  pendown()
  forward(length * 1.5)
  right(45)
  draw(length)
  left(90)
  pendown()
  draw(length)
  right(45)
  backward(length * 1.5)
  left(360 / number_of_arms)

penup()
setheading(90) # North
forward(100)

done()  # this releases the motors to save power
