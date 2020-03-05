from turtle import *
import calibration
from time import sleep

global scale
global frac_error

setDebug(True)  # True print commands on serial console
# Place turtle in lower left of paper facing east.

print('\nRunning "turtle_wheel_calibration.py".\n')
print('The following parameters are saved in "lib/calibration.py":')
print('    wheel_dia = %s mm (increase = decrease distance)' % calibration.wheel_dia)
print('    wheel_base = %s mm (increase = spiral in) ' % calibration.wheel_base)
print('    PEN_UP angle = %s' % calibration.PEN_UP)
print('    PEN_DOWN angle = %s' % calibration.PEN_DOWN)


# Test the servo
for x in range(2):
    penup()
    sleep(1)
    pendown()
    sleep(1)

# draw four squares to determine if wheel parameters are correct
for turns in range(4):
	for x in range(4):
		forward(100)
		left(90)

penup()
sleep(1)
done()
