import board
import simpleio
import time

PIEZO_PIN = board.D5


simpleio.tone(PIEZO_PIN, 440, duration=1)
time.sleep(0.5)


# play random notes on startup
for x in range(5):
    frequency = random.random()*800+100
    duration = random.random()/16
    simpleio.tone(PIEZO_PIN, frequency, duration=duration)

while True:
    pass
