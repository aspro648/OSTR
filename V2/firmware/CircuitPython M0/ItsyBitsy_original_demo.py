# Itsy Bitsy M0 Express IO demo
# Welcome to CircuitPython 2.2 :)

import board
import gc
import time
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
import audioio
import touchio
import pulseio
import neopixel
import adafruit_dotstar
from adafruit_motor import servo

gc.collect()   # make some rooooom
# HID keyboard support
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# One pixel connected internally!
dot = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.5)

# Built in red LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# Analog audio output on A0, using two audio files
audiofiles = ["rimshot.wav", "laugh.wav"]

# Analog input on A1
analog1in = AnalogIn(board.A1)

# Capacitive touch on A2
touch = touchio.TouchIn(board.A2)

# Digital input with pullup on D7, D9, and D10
buttons = []
for p in [board.D7, board.D9, board.D10]:
    button = DigitalInOut(p)
    button.direction = Direction.INPUT
    button.pull = Pull.UP
    buttons.append(button)

# Servo on D12
servo_pwm = pulseio.PWMOut(board.D12, frequency=50)
servo = servo.Servo(servo_pwm)

# NeoPixel strip (of 16 LEDs) connected on D5
NUMPIXELS = 16
neopixels = neopixel.NeoPixel(board.D5, NUMPIXELS, brightness=0.2, auto_write=False)

# Used if we do HID output, see below
kbd = Keyboard()

######################### HELPERS ##############################

# Helper to convert analog input to voltage
def getVoltage(pin):
    return (pin.value * 3.3) / 65536

# Helper to give us a nice color swirl
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return [0, 0, 0]
    if (pos > 255):
        return [0, 0, 0]
    if (pos < 85):
        return [int(pos * 3), int(255 - (pos*3)), 0]
    elif (pos < 170):
        pos -= 85
        return [int(255 - pos*3), 0, int(pos*3)]
    else:
        pos -= 170
        return [0, int(pos*3), int(255 - pos*3)]

def play_file(filename):
    print("")
    print("----------------------------------")
    print("playing file "+filename)
    f = open(filename, "rb")
    a = audioio.AudioOut(board.A0, f)
    a.play()
    while a.playing:
        pass
    print("finished")
    print("----------------------------------")
    
######################### MAIN LOOP ##############################

i = 0
while True:
  # spin internal LED around! autoshow is on
  dot[0] = wheel(i & 255)

  # also make the neopixels swirl around
  for p in range(NUMPIXELS):
      idx = int ((p * 256 / NUMPIXELS) + i)
      neopixels[p] = wheel(idx & 255)
  neopixels.show()

  # Read analog voltage on A1
  print("A1: %0.2f" % getVoltage(analog1in), end="\t")

  # use A2 as capacitive touch to turn on internal LED
  print("A2 touch: %d" % touch.raw_value, end="\t")
  if touch.value:
      print("A2 touched!", end ="\t")
  led.value = touch.value

  if not buttons[0].value:
      print("Button D7 pressed!", end ="\t")
      # optional! uncomment below & save to have it sent a keypress
      #kbd.press(Keycode.A)
      #kbd.release_all()

  if not buttons[1].value:
      print("Button D9 pressed!", end ="\t")
      play_file(audiofiles[0])

  if not buttons[2].value:
      print("Button D10 pressed!", end ="\t")
      play_file(audiofiles[1])

  # sweep a servo from 0-180 degrees (map from 0-255)
  servo.angle = i / 255 * 180
  
  i = (i+1) % 256  # run from 0 to 255
  #time.sleep(0.01) # make bigger to slow down

  print("")
