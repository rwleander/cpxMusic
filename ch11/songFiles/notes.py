#  Python code for Making Music with the Circuit Playground Express
#    by Rick Leander
#    Copyright (c) 2020 Rick Leander All rights reserved
#

# notes library - play tunes using list of notes or text file


import time

# songs

scale = 'C,D,E,F,G,A,B,C5' 
scale3 = 'C3,D3,E3,F3,G3,A3,B3,C4,D4,E4,F4,G4,A4,B4,C5,D5,E5,F5,G5,A5,B5,C6'
chromatic_scale = 'C,C#,D,D#,E,F,F#,G,G#,A,A#,B,C5'
birthday = 'C:0.75,C:0.25,D,C,F,E:2, C:0.75,C:0.25,D,C,G,F:2, C:0.75,C:0.25,C5,A,F,E,D:2, Bb:0.75,Bb:0.25,A,F,G,F:4'
mary = 'E,D,C,D,E,E,E:2, D,D,D:2, E,G,G:2, E,D,C,D,E,E,E,E, D,D,E,D,C:4'
twinkle = 'C,C,G,G,A,A,G:2, F,F,E,E,D,D,C:2,G,G,F,F,E,E,D:2, G,G,F,F,E,E,D:2, C,C,G,G,A,A,G:2, F,F,E,E,D,D,C:4'

# frequencies for notes


C = 261.63
Cs = 277.18
Df = Cs
D = 293.66
Ds = 311.13
Ef = Ds
E = 329.63
F = 349.23
Fs = 369.99
Gf = Fs
G = 392.00
Gs = 415.30
Af = Gs
A = 440.00
As = 466.16
Bf = As
B =493.88

pitch_list = {'C': C, 'C#': Cs, 'Db': Df, 'D': D, 'D#': Ds, 'Eb': Ef, 'E': E, 'F': F, 'F#': Fs, 'Gb': Gf, 'G': G, 'G#': Gs, 'Ab': Af, 'A': A, 'A#': As, 'Bb': Bf, 'B': B}
pitch = {}

duration = 0.25

# build an array of notes and frequencies

for key, val in pitch_list.items():
  pitch[key] = val
  pitch [key + '3'] = val /2
  pitch [key + '4'] = val
  pitch [key + '5'] = val * 2
pitch['C6'] = C * 4
 
# calculate tempo from beats per minute

def set_tempo (bpm):
  duration = 60 / bpm

# play a sequence

def play (cp, song):
  items = song.split(',')
  for item in items:
    parts = item.split(':')
    note = parts[0].strip()
    tone  = 0
    if note in pitch:
      tone = pitch[note]
    if len (parts) > 1:
      length = float(parts[1].strip()) * duration
    else:
      length = duration
    if tone > 0:
      cp.play_tone (tone, length)
    else:
      time.sleep (length)

# play song from file

def play_file (cp, file_name):
  with open (file_name, 'r') as fl:
    for txt in fl:
      if txt > '':
        play (cp, txt)
        
