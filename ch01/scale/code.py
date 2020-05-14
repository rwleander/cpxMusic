#  Python code for Make Music with the Circuit Playground Express
#    by Rick Leander
#    Copyright (c) 2020 Rick Leander All rights reserved
#

# play the C major scale

from adafruit_circuitplayground import cp

tempo = 0.5

cp.play_tone(261.63, tempo)
cp.play_tone(293.66, tempo)
cp.play_tone(329.63, tempo)
cp.play_tone(349.23, tempo)
cp.play_tone(392.00, tempo)
cp.play_tone(440.00, tempo)
cp.play_tone(493.88, tempo)
cp.play_tone(523.26, tempo)
