import board

import simpleio


# Define pin connected to piezo buzzer.
PIEZO_PIN = board.A0

# Define a list of tones/music notes to play.
TONE_FREQ = [ 262,  # C4
              294,  # D4
              330,  # E4
              349,  # F4
              392,  # G4
              440,  # A4
              494 ] # B4


# Main loop will go through each tone in order up and down.
for x in range(1):
    # Play tones going from start to end of list.
    for i in range(len(TONE_FREQ)):
        simpleio.tone(PIEZO_PIN, TONE_FREQ[i], duration=0.25)
    # Then play tones going from end to start of list.
    for i in range(len(TONE_FREQ)-1, -1, -1):
        simpleio.tone(PIEZO_PIN, TONE_FREQ[i], duration=0.25)