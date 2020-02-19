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

print('Example of using vector fonts from turtle_font.py')


backward(75)
left(90)
backward(25)
right(90)

pendown()
setScale(13)

H()
E()
L()
L()
O()

penup()
setheading(90) # North
forward(100)
done()



