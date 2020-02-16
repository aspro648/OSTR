import board
import simpleio
import random

PIEZO_PIN = board.A0


def tone(frequency, duration):
    ''' Plays a single note of frequency (hz)
        and duration (seconds). '''
    simpleio.tone(PIEZO_PIN, frequency, duration=duration)


# play 3 random notes on startup
for x in range(3):
    frequency = random.random()*800+100
    duration = random.random()/8
    tone(frequency, duration)
    print("tone(%s, %s)" % (frequency, duration))