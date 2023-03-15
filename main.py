from music21 import converter, instrument, note, chord, environment

# Configure the music21 environment to use a suitable music notation software
# env = environment.Environment()
# env['musicxmlPath'] = 'path/to/your/music-notation-software-executable'
# env['musescoreDirectPNGPath'] = env['musicxmlPath']

def read_midi_file(file_path):
    # Read the MIDI file using the music21 converter
    midi = converter.parse(file_path)

    # Get a list of all the instruments in the MIDI file
    parts = instrument.partitionByInstrument(midi)

    # Extract notes and chords from each instrument
    notes_to_parse = parts.parts[0].recurse()

    # Iterate through the notes and chords, and store them in a list
    notes = []
    for element in notes_to_parse:
        if isinstance(element, note.Note):
            notes.append(str(element.pitch))
        elif isinstance(element, chord.Chord):
            notes.append('.'.join(str(n) for n in element.normalOrder))

    return midi, notes

# Replace with the path to your MIDI file
midi_file_path = "assets/Never-Gonna-Give-You-Up-1.mid"

midi, notes = read_midi_file(midi_file_path)
print("Notes and chords in the MIDI file:")
print(notes)

# Show the sheet music for the MIDI file
midi.show()
