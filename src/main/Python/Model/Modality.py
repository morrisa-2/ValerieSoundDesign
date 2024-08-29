"""
Models a musical mode.
"""

from enum import Enum

class Modes(Enum):

    IONIAN = [2, 2, 1, 2, 2, 2, 1]
    DORIAN = [2, 1, 2, 2, 2, 1, 2]
    PHRYGIAN = [1, 2, 2, 2, 1, 2, 2]
    LYDIAN = [2, 2, 2, 1, 2, 2, 1]
    MIXOLYDIAN = [2, 2, 1, 2, 2, 1, 2]
    AEOLIAN = [2, 1, 2, 2, 1, 2, 2]
    LOCRIAN = [1, 2, 2, 1, 2, 2, 2]

class Modality:

    def __init__(self, mode):
        if mode not in Modes:
            raise Exception("Unrecognized mode.")
        else:
            self._mode = mode

    def __len__(self):
        return len(self._mode)

    def __getitem__(self, item):
        return self._mode[item]
