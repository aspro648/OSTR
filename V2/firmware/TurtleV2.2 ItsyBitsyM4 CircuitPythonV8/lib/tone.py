import board
import simpleio
import random
import settings


PIEZO_PIN = settings.speakerPin


def tone(frequency, duration):
    ''' Plays a single note of frequency (hz)
        and duration (seconds). '''
    simpleio.tone(PIEZO_PIN, frequency, duration=duration)


# play random notes on startup
for x in range(5):
    frequency = random.random()*800+100
    duration = random.random()/16
    #tone(frequency, duration)
    simpleio.tone(PIEZO_PIN, frequency, duration=duration)
    if False: print("tone(%s, %s)" % (frequency, duration))
