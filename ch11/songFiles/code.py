#  Python code for Making Music with the Circuit Playground Express
#    by Rick Leander
#    Copyright (c) 2020 Rick Leander All rights reserved
#

#  play a song from a file

from adafruit_circuitplayground import cp
import notes

# main loop

notes.set_tempo(90)
while True:
  if cp.button_a:
    notes.play_file(cp, 'song.txt')
	