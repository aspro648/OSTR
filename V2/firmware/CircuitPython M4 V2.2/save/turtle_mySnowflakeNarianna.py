from turtle import *

'''
Learn how to make a snowflake at
https://groklearning.com/hoc/activity/snowflake/

This code will run on the Turtle Robot or on a laptop.
Pensize() & color() are not implemented in robot, but will
not cause an error.

See turtle_snowflake_example.py for simple example.
'''

print('Running "mySnowflake.py"')


# Place your code from https://groklearning.com/hoc/activity/snowflake/ here:
from turtle import *
pendown()
for i in range(6):
  pensize(5)
  pencolor('skyblue')
  forward(100)
  left(45)
  forward(50)
  backward(50)
  right(90)
  forward(50)
  backward(50)
  left(45)
  forward(50)
  left(45)
  forward(50)
  backward(50)
  right(90)
  forward(50)
  backward(50)
  left(45)
  backward(100)
  right(60)



done()  # this releases the motors to save power