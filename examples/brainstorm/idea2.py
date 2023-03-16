from pymusic import Synth, Note, Chord, Pattern, TempoClock

Synth()

synth_def = Synth.create_def('simple_sine', {
    "arg": {"freq":440, "amp":0.5, "gate":1},
    "var": ["env", "sig"],
    "env": EnvGen.kr(Env.asr(0.01, 1, 0.5), gate, doneAction: 2),
    "sig": SinOsc.ar(freq) * env * amp,
    Out.ar(0, sig),
})

# Instantiate a Synth object
sine_synth = Synth(synth_def)

# Create notes and chords
note_c = Note('C4')
chord_c_major = Chord('C4', 'major')

# Create a pattern with list comprehension
pattern = Pattern([note_c] + chord_c_major.notes)

# Set up a tempo clock
clock = TempoClock(bpm=120)

# Function to play a sequence of notes
def play_sequence(synth, notes, duration=0.5):
    for note in notes:
        synth.play(freq=note.frequency, amp=0.5, gate=1)
        clock.wait(duration)
        synth.release()

# Live coding example
while True:
    # Play the pattern
    play_sequence(sine_synth, pattern.notes, duration=0.25)

    # Play an arpeggio using list comprehension
    arpeggio = [note.transpose(i * 12) for note in chord_c_major.notes for i in range(3)]
    play_sequence(sine_synth, arpeggio, duration=0.125)

    # Play a sequence of random chords using dict comprehension
    random_chord_sequence = [Chord(root, quality) for root, quality in [('C4', 'major'), ('G4', 'minor'), ('A4', 'minor'), ('F4', 'major')]]
    for chord in random_chord_sequence:
        play_sequence(sine_synth, chord.notes, duration=0.25)
