from supriya.ugens import EnvGen, Out, SinOsc
from supriya.synthdefs import Envelope, synthdef

import supriya

@synthdef
def sine_synth(frequency=440, amplitude=0.5):
    sine_wave = SinOsc.ar(frequency=frequency)
    audio_out = Out.ar(bus=0, source=sine_wave * amplitude)
    return audio_out


def play_sine_wave(frequency=440, duration=5):
    server = supriya.Server.boot()
    server.add_synth(sine_synth)
    

if __name__ == "__main__":
    play_sine_wave(frequency=440, duration=5)
