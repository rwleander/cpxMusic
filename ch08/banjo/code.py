#  Python code for Make Music with the Circuit Playground Express
#    by Rick Leander
#  Copyright (c) 2020 Rick Leander All rights reserved
#  Buy the book at https://www.amazon.com/author/rleander#
#
# touch pad banjo

from adafruit_circuitplayground import cp

# notes and frequencies

C = 261.63
D = 293.66
E = 329.63
Fs = 369.99
G = 392.00
A = 440.00
B =493.88

g_chord = [G, B, D * 2, G]
c_chord = [C, E, G, E]
d_chord = [D, Fs, A, Fs]

tempo = 0.03

# function to play chord

def play_chord(chord):
  for note in chord:
    cp.play_tone(note, tempo)

# main loop

while True:
  if cp.touch_A1:
    play_chord(g_chord)
  if cp.touch_A3:
    play_chord(c_chord)
  if cp.touch_A4:
    play_chord(d_chord)
      
      