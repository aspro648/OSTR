import simpleio
import random
import settings


PIEZO_PIN = settings.speakerPin

DEBUG = False
print('Running "%s" to play startup notes!' % __file__)


# play random notes on startup
for x in range(5):
    frequency = random.random()*800+100
    duration = random.random()/16
    simpleio.tone(PIEZO_PIN, frequency, duration=duration)
    if DEBUG: print("tone(%s, %s, duration=%.3f)" % (PIEZO_PIN, frequency, duration))


'''
Explore:
    * What is the highest and lowest frequency tone you can hear?
        - Does that correspond with what you expect?
        - Look at the datasheet for the speaker to see if it has clues.
    * You can see in the documentation that the duration is optional.  What happens if you omit it?
    * Open Example_04_music.py and make a tune.
    * In the early days of cell phones, a system called Ring Tone Text Transfer Language (rtttl)
      was developed by Nokia to play tunes.
        - Open Example_04_rtttl.py and examine the available tunes.
'''
