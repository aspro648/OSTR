import board
import digitalio
import time
import pwmio

# define pins used
led = pwmio.PWMOut(board.D2, frequency=5000, duty_cycle=0)


while True:
    for i in range(0, 65535, 10):
        led.duty_cycle = i
    for i in range(65535, 0, -10):
        led.duty_cycle = i
