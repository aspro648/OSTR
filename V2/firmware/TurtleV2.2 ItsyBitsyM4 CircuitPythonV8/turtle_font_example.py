from turtle import *
from time import sleep

try:
    from lib.turtle_font import *
except ImportError:
    import sys
    print('\nError: Need file "lib/turtle_font.py"')
    sys.exit()

'''
Place turtle in center of paper facing east.

This code will run on the Turtle Robot or on a laptop.
Pensize() & color() are not implemented in robot, but will
not cause an error.
'''

print('Running "%s"' % __file__)

pensize(2)          # pensize & color are not implemented in robot
pencolor('skyblue')

# Upper case letters, numbers, punctuation only.
text = "HELLO!"


#move turtle on page
penup()
backward(75)
left(90)
backward(25)
right(90)

setScale(10)  # scale 10 letters are 20mm width by 40mm high

for letter in text:
    func_to_call = fDict.get(letter.upper())
    try:
        func_to_call()
    except TypeError:
        print("No font for '%s'." % letter)

# Move turtle out of the way
penup()
setheading(90) # North
forward(100)
done()


