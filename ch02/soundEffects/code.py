#  Python code for Making Music with the Circuit Playground Express
#    by Rick Leander
#    Copyright (c) 2020 Rick Leander All rights reserved
#

# play the wave files found on the board

from adafruit_circuitplayground import cp
import os

# find the .wav files and put them into a list

files = os.listdir()
wavs = []
for file in files:
  if (file.endswith('.wav')):
    wavs.append(file)
  
#main loop

i = 0
while True:
  if cp.button_a:  
    cp.play_file(wavs[i])
  
  if cp.button_b:
    i = i + 1
    if i >= len(wavs):
      i = 0
    cp.play_file(wavs[i])
      
	