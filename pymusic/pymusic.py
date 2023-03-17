from abc import ABC, abstractmethod
from typing import List, Any
from random import choice

class pyMusicObj(ABC):
    pass

class Synth(pyMusicObj):
    ...

class Note(pyMusicObj):
    ...

class Chord(pyMusicObj):
    ...

class Scale(pyMusicObj):
    ...

class Pattern(pyMusicObj):
    ...

class HarmonicSeries(pyMusicObj):
    ...

class Tonality(pyMusicObj):
    ...

class Synth(pyMusicObj):
    def __init__(self, synth_name:str) -> None:
        super().__init__()
        self.synth_name = synth_name
    
    def play(self, pattern:Pattern, duration:float=1.0) -> None:
        # probably needs to be async
        pass

class Note(pyMusicObj):
    def __init__(self, name:str) -> None:
        super().__init__()
        self.name = name

class Pattern(pyMusicObj):
    def __init__(self, items:List[Any]) -> None:
        super().__init__()
        self.items = items

class Chord(Pattern):
    def __init__(self, root:Note, tonality:Tonality, octaves=4) -> None:
        super().__init__()

class Scale(Pattern):
    def __init__(self, root:Note, tonality:Tonality, octaves=4) -> None:
        super().__init__()

class HarmonicSeries(Pattern):
    def __init__(self, root:Note, n_harmonics:int) -> None:
        super().__init__()
        self.root = root
        self.n_harmonics = n_harmonics


def main():
    key = Note('C4')
    tonality = Tonality('major')
    scale = Scale(key.root, tonality)
    s1 = Synth('sine')

    # Create a pattern with list comprehension
    pattern = Pattern([key.root] + [choice(scale.notes) for _ in range(16)])

    # Function to play a sequence of notes
    s1.play(pattern, duration=4.0)

if __name__ == '__main__':
    main()
