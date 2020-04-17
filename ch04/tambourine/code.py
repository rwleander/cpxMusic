#  Python code for Making Music with the Circuit Playground Express
#    by Rick Leander
#    Copyright (c) 2020 Rick Leander All rights reserved
#

# shake or tap for tambourine sounds

from adafruit_circuitplayground import cp

# wave files

tap = 'hi_snare.wav'
shake = 'cymbal.wav'

# main loop

cp.detect_taps = 1
while True:
  if cp.tapped:
    cp.play_file(tap)
  if cp.shake(shake_threshold=15):
    cp.play_file(shake)
      