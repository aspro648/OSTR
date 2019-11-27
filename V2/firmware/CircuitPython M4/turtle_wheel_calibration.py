from turtle import *
global scale
from time import sleep


print('\nRunning "turtle_wheel_calibration.py".\n')
print('The following parameters are saved in "lib/turtle.py":')
print('    wheel_dia = %s mm (increase = decrease distance)' % wheel_dia)
print('    wheel_base = %s mm (increase = spiral in) ' % wheel_base)
print('    PEN_UP angle = %s' % PEN_UP)
print('    PEN_DOWN angle = %s' % PEN_DOWN)

pendown()
sleep(1)

# draw four squares to determine if wheel parameters are correct
for turns in range(1):
	for x in range(4):
		forward(100)
		right(90)

penup()
done()