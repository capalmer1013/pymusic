from random import choice

from pymusic import Synth, Note, Chord, Scale, Pattern, HarmonicSeries

# Pattern->Scale
# Pattern->Chord

key = Scale('C4', 'major', octaves=2)
hs = HarmonicSeries(key.root, 4)
s1 = Synth('simple_sine')

# Create a pattern with list comprehension
pattern = Pattern([key.root] + [choice(key.notes) for _ in range(16)])

# Function to play a sequence of notes
s1.play(pattern, duration=4.0)





# =============================================================
# example micro-language-like syntax

from pymusic.notes import A, B, C, D, E, F, G
from pymusic.tonality import major, minor
from pymusic.synth import sine, sawtooth, square, triangle

from pymusic import Pattern, Synth, Note, Chord, Scale, HarmonicSeries

# someting using mostly symbols
# () >> << ^ * % & | + - / = ! ? : ; , . [ ] { } @ ~ ` #

Pattern = [x for x in Scale(C, major).random(16)] >> sine >> 4.0
Synth.play(Pattern)
