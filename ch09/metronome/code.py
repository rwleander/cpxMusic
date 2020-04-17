#  Python code for Making Music with the Circuit Playground Express
#    by Rick Leander
#    Copyright (c) 2020 Rick Leander All rights reserved
#

# metronome with slide switch, buttons and lights

from adafruit_circuitplayground import cp
import time

# initial settings

bpm = 60
tone = 440

# colors

red = [64, 0, 0]
green = [0, 64, 0]
blue = [0, 0, 64]
colors = [red, green, blue]

  # calculate delay

def get_delay (bpm):
  return 1.0 / (bpm / 60) - 0.1

# set new bpm and delay after button press
  
def set_bpm (bpm):
  if bpm < 10:
    bpm = 10
  if bpm > 290:
    bpm = 290
  return bpm

# set colors

def set_color (bpm):
  i = int(bpm / 30) 
  c = int ((bpm / 10) % 3)
  cp.pixels.fill (0)
  cp.pixels[i] = colors[c]
  
# main loop

delay = get_delay(bpm)
set_color (bpm)
while True:
  if cp.button_a:
    bpm= set_bpm(bpm - 10)
    delay = get_delay(bpm)
    set_color (bpm)
  if cp.button_b:
    bpm= set_bpm(bpm + 10)
    delay = get_delay(bpm)
    set_color (bpm)
  if cp.switch == False:
    cp.pixels.brightness = 0.5 
    cp.play_tone (tone, 0.1)
    cp.pixels.brightness = 0
  time.sleep (delay)
  