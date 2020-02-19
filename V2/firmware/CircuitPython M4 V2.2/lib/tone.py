import board
import simpleio
import random

PIEZO_PIN = board.A0


def tone(frequency, duration):
    ''' Plays a single note of frequency (hz)
        and duration (seconds). '''
    simpleio.tone(PIEZO_PIN, frequency, duration=duration)


# play random notes on startup
for x in range(5):
    frequency = random.random()*800+100
    duration = random.random()/16
    tone(frequency, duration)
    if False: print("tone(%s, %s)" % (frequency, duration))
