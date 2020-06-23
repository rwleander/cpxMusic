#  Python code for Make Music with the Circuit Playground Express
#    by Rick Leander
#  Copyright (c) 2020 Rick Leander All rights reserved
#  Buy the book at https://www.amazon.com/author/rleander#
#

#  cowbell  using touch pad

from adafruit_circuitplayground import cp

# main loop

while True:
    if cp.touch_A3:
        cp.play_file ('cowbell.wav')
    