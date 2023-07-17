'''
#https://github.com/dhylands/upy-rtttl
The MIT License (MIT)

Copyright (c) 2016 Dave Hylands
Copyright (c) 2017 David Glaude

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from rtttl import RTTTL
import songs

import board
import simpleio
import time

speaker_pin  = board.A0  # Speaker is connected to this DIGITAL pin

# Initialize input/output pins
#pwm       = pulseio.PWMOut(speaker_pin, variable_frequency=True, duty_cycle=0)

def play_tone(freq, msec):
    print('freq = {:6.1f} msec = {:6.1f}'.format(freq, msec))
    simpleio.tone(speaker_pin, freq, duration=msec/1500)
    '''
    if freq > 0:
        pwm.frequency  = int(freq)   # Set frequency
        pwm.duty_cycle = 32767  # 50% duty cycle
	time.sleep(msec*0.001)  # Play for a number of msec
    pwm.duty_cycle = 0          # Stop playing
    '''
    #time.sleep(0.05)            # Delay 50 ms between notes

# Code for these tunes are contained in lib/songs.py
song_names = ['Super Mario - Main Theme', 'Super Mario - Title Music', 'SMBtheme', 'SMBwater',
              'SMBunderground', 'Picaxe', 'The Simpsons', 'Indiana', 'TakeOnMe', 'Entertainer',
              'Muppets', 'Xfiles', 'Looney', '20thCenFox', 'Bond', 'MASH', 'StarWars', 'GoodBad',
              'TopGun', 'A-Team', 'Flinstones', 'Jeopardy', 'Gadget', 'Smurfs', 'MahnaMahna',
              'LeisureSuit', 'MissionImp', 'RickAstley']

tune = RTTTL(songs.find('Entertainer'))

time.sleep(2) # separate from startup beeps

for freq, msec in tune.notes():
    play_tone(freq, msec)
