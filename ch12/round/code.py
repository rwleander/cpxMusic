#  Python code for Make Music with the Circuit Playground Express
#    by Rick Leander
#    Copyright (c) 2020 Rick Leander All rights reserved
#

# play on two speakers


from adafruit_circuitplayground import cp
import board
import pulseio
import time

# fill in song variables

song = 'C:4,C:4,C:3,D,E:4, E:3,D,E:3,F,G:8, C5:3,C5,G:3,G,E:3,E,C:3,C, G:3,F,E:3,D,C:8,'
song1 = song + song + song + ',:16'
song2 = ':16,' + song + song + song
notes1 = song1.split(',')
notes2 = song2.split(',')

# frequencies for notes

C = 261.63
D = 293.66
E = 329.63
F = 349.23
G = 392.00
A = 440.00
B =493.88

pitch= {'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'A': A, 'B': B, 'C5': C * 2}

duration = 0.1


# play a tone on the speaker

speaker  = pulseio.PWMOut(board.A3, duty_cycle=0, frequency=440, variable_frequency=True)

def start_speaker(tone):
  time.sleep(0.05)
  speaker.frequency = int(tone)
  speaker.duty_cycle = 6553 
    
#  stop the speaker
def stop_speaker():
  speaker.duty_cycle = 0

# break apart a note

def get_note (note):
  parts = note.split(':')
  part1 = parts[0].strip()
  tone  = 0
  if part1 in pitch:
    tone = pitch[part1]
  length = 1
  if len (parts) > 1:
    length = float(parts[1].strip())  
  return [tone, length]
  
  
# play the song

[tone1, length1] = get_note(notes1[0])
[tone2, length2] = get_note(notes2[0])
last_tone1 = 0
last_tone2 = 0
n1 = 0
n2 = 0

while n1 < len(notes1) or  len2 < len(notes2):  
  if tone1 != last_tone1:
    if tone1 > 0:
      cp.start_tone(tone1)
  if tone2 != last_tone2:
    if tone2 > 0:
      start_speaker(tone2)      
      
  time.sleep(duration)
  
  last_tone1 = tone1
  last_tone2 = tone2
  length1 = length1 - 1
  length2 = length2 - 1
  
  if length1 <= 0:
    cp.stop_tone()
    n1 = n1 + 1
    [tone1, length1] = get_note(notes1[n1]) 
    last_tone1 = 0
    
  if length2 <= 0:
    stop_speaker()
    n2 = n2 + 1
    [tone2, length2] = get_note(notes2[n2])
    last_tone2 = 0

cp_stop_tone()
speaker_off()
              
      
  