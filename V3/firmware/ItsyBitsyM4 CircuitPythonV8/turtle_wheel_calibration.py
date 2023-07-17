from turtle import *
from time import sleep


setDebug(True)  # True print commands on serial console
# Place turtle in lower left of paper facing east.

print('\nRunning "turtle_wheel_calibration.py".\n')

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
		right(90)

penup()
sleep(1)
done()
