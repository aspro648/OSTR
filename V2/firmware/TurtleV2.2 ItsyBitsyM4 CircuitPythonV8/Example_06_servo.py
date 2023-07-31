# https://learn.adafruit.com/circuitpython-essentials/circuitpython-servo

import pwmio
import settings
from adafruit_motor import servo
from time import sleep

print('Running "%s"' % __file__)

servoPin = settings.servoPin

# create a PWMOut object on the correct Pin
pwm = pwmio.PWMOut(servoPin, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(45, 135, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        sleep(0.05)
    for angle in range(135, 45, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        sleep(0.05)

'''
Explore:
    * If you don’t remember what the for-loop is doing, try the following in the REPL console:
        for angle in range(0, 180, 5):print(angle)
    * Can you modify the code so that the servo moves when a button is pushed?
        - reuse code from Example_02_button.py

'''
