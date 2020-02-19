import board
import time
import simpleio
from tone import tone

'''
Can you adapt your favorite tune to code?
Add notes / frequencies from https://pages.mtu.edu/~suits/notefreqs.html

If you don't want to hear startup beeps, modify lib/tone.py
'''


# note / frequency
C4 = 262
D4 = 294
E4 = 330
F4 = 349
G4 = 392
A4 = 440
B4 = 494

# This is a list of tuples, i.e. (note, duration)
tune = [(C4, 0.25), (D4, 0.25), (E4, 0.25), (F4, 0.25), (G4, 0.25),
        (A4, 0.25), (B4, 0.25)]

time.sleep(2) # wait for startup beeps to end

for note in tune:
    frequency, duration = note # unpack the tuple
    tone(frequency, duration)
