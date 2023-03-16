from random import choice

from pymusic import Synth, Note, Chord, Scale, Pattern

# Pattern->Scale
# Pattern->Chord

key = Scale('C4', 'major', octaves=2)
s1 = Synth('simple_sine')

# Create a pattern with list comprehension
pattern = Pattern([key.root] + [choice(key.notes) for _ in range(16)])

# Function to play a sequence of notes
s1.play(pattern, duration=4.0)
