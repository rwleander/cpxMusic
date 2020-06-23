#  Python code for Make Music with the Circuit Playground Express
#    by Rick Leander
#  Copyright (c) 2020 Rick Leander All rights reserved
#  Buy the book at https://www.amazon.com/author/rleander#
#
#  play a song from a file

from adafruit_circuitplayground import cp
import notes

# main loop

notes.set_tempo(90)
while True:
  if cp.button_a:
    notes.play_file(cp, 'song.txt')
	