#  Python code for Making Music with the Circuit Playground Express
#    by Rick Leander
#    Copyright (c) 2020 Rick Leander All rights reserved
#

# Touch flute

from adafruit_circuitplayground import cp
import time

# notes and frequencies

C = 261.63
D = 293.66
E = 329.63
F = 349.23
G = 392.00
A = 440.00
B =493.88

octave = 2

# main loop

cp.adjust_touch_threshold(200)
lastTone = 0
while True:  
  tone = 0
  a1 = cp.touch_A1
  a2 = cp.touch_A2
  a3 = cp.touch_A3
  a4 = cp.touch_A4
  a5 = cp.touch_A5
  a6 = cp.touch_A6
  
  if a1 and a2:
    tone = D
  elif a2 and a3:
    tone = F
  elif a4 and a5:
    tone = B
  elif a1:
    tone = C
  elif a2:
    tone = E
  elif a3:
    tone = G
  elif a4:
    tone = A
  elif a5:
    tone = C * 2    
    
  if a6:
    tone = tone * 2      
    
  tone = tone * octave
  if tone != lastTone: 
    if tone > 0:
      cp.start_tone (tone)
    else: 
      cp.stop_tone()
    
  lastTone = tone
  time.sleep (0.1)
  