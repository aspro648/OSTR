from turtle import *
try:
    from turtle_font import *
except ImportError:
    import sys
    print('\nError: Need file "/lib/turtle_font.py"')
    sys.exit()

'''
This code will run on the Turtle Robot or on a laptop.
Pensize() & color() are not implemented in robot, but will
not cause an error.
'''

print('Example of using vector fonts from turtle_font.py')

pendown()
setScale(10)

H()
E()
L()
L()
O()

penup()
done()



