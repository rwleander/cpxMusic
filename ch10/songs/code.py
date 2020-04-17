#  Python code for Making Music with the Circuit Playground Express
#    by Rick Leander
#    Copyright (c) 2020 Rick Leander All rights reserved
#

#  play a song

from adafruit_circuitplayground import cp
import notes

song = 'C:0.75,C:0.25,D,C,F,E:2, C:0.75,C:0.25,D,C,G,F:2, C:0.75,C:0.25,C5,A,F,E,D:2, Bb:0.75,Bb:0.25,A,F,G,F:4'

# main loop

notes.set_tempo(90)
while True:
  if cp.button_a:
    notes.play(cp, song)
  if cp.button_b:
    notes.play(cp, notes.mary)
  