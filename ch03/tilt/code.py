#  Python code for Make Music with the Circuit Playground Express
#    by Rick Leander
#  Copyright (c) 2020 Rick Leander All rights reserved
#  Buy the book at https://www.amazon.com/author/rleander#
#
# use accelerometer to play sounds

from adafruit_circuitplayground import cp

# notes and frequencies

C = 261.63
D = 293.66
E = 329.63
F = 349.23
G = 392.00
A = 440.00
B =493.88

notes = [C / 2, D / 2, E / 2, F / 2, G / 2, A / 2, B / 2, C, D, E, F, G, A, B, C * 2, D * 2, E * 2, F * 2, G * 2, A * 2, B * 2, C * 3]

# main loop

while True:  
  if cp.switch == False:
    [x, y, z] = cp.acceleration
    i  = 11 - int (x)
    delay = 0.25 + (y / 50.0)
    cp.play_tone(notes[i], delay)    
      
    