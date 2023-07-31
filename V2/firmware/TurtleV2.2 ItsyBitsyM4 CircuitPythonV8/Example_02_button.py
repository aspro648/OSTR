import board
import digitalio


print('Running "%s"' % __file__)

# define pins used
right_led = digitalio.DigitalInOut(board.D7)
button = digitalio.DigitalInOut(board.D12)

# assign pins as input or output
right_led.direction = digitalio.Direction.OUTPUT
button.switch_to_input(pull=digitalio.Pull.UP)

while True:
    if button.value:
        right_led.value = False
    else:
        right_led.value = True

'''
Explore:
    * What happens if we change “if button.value” to “if not button.value”?
    * Add code so that one LED turns off when the other turns off.
    * Research the functions time.monotonic() and random.random().
    *Can you code a reaction time tester?
        - Wait a random period and then turn the LED on.
        - Measure the time until the button is pressed.
        - Calculate the time between the LED turning on and the button press.
'''
