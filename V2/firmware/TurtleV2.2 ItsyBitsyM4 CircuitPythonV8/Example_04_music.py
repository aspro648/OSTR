import simpleio
import random
import settings
from time import sleep


PIEZO_PIN = settings.speakerPin

'''
Can you adapt your favorite tune to code?
Add notes / frequencies from https://pages.mtu.edu/~suits/notefreqs.html
'''

DEBUG = True
if DEBUG: print('Running "%s"' % __file__)

# note / frequency
C4 = 262
D4 = 294
E4 = 330
F4 = 349
G4 = 392
A4 = 440
B4 = 494

# This is a list of tuples, i.e. (note, duration)
tune = [(C4, 0.5), (D4, 0.4), (E4, 0.3), (F4, 0.2), (G4, 0.1),
        (A4, 0.075), (B4, 0.05)]

sleep(2)  # wait for startup beeps to end

for note in tune:
    frequency, duration = note  # unpack the tuple
    if DEBUG: print("tone(%s, %s)" % (frequency, duration))
    simpleio.tone(PIEZO_PIN, frequency, duration=duration)

for note in tune[::-1]:  # list[::-1] reverses the order
    frequency, duration = note  # unpack the tuple
    if DEBUG: print("tone(%s, %s)" % (frequency, duration))
    simpleio.tone(PIEZO_PIN, frequency, duration=duration)
