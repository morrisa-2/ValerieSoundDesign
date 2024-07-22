"""
A simple synth patch for the gensound module.
"""

from gensound import Sine
from gensound import Gain
from gensound import ADSR
from pathlib import Path

class Synth:

    def _dropOctave(self,variation):
        """
        Drops the pitch of each note in the given variation
        by a single octave.
        :param variation: Variation to drop pitches of.
        :return: A string of the variation's notes pitched
        down an octave.
        """
        notes = variation.prepForSignal()[0]
        return "@transpose:-12.0 " + notes

    def generateSignal(self,variation,order,filePath):
        """
        Exports the given variation as a wav file.
        :param variation: Variation to play.
        :param order: Ordinal listing of placement in batch,
        starting from 0.
        :param filePath: Path to export the wav file to,
        as either a String or Path object.
        """
        pathIsString = isinstance(filePath,str)
        if pathIsString:
            filePath = Path(filePath)
        if not filePath.exists():
            raise NameError("Please enter an existing path.")
        if not filePath.is_dir():
            raise TypeError("Please enter a path to a directory.")
        else:
            unpackedVariation = variation.prepForSignal()
            sig1 = Sine(unpackedVariation[0],duration=unpackedVariation[1]) * Gain(-4)
            downAnOctave = self._dropOctave(variation)
            sig2 = Sine(downAnOctave,duration=unpackedVariation[1]) * Gain(-4)
            sig = sig1 + sig2
            #TODO: Fix ADSR transform
            #ADSR makes the amplitude freak out sometimes--fix and then uncomment.
            #sig = sig * ADSR(attack=0.05e3, decay=0.02e3, sustain=0.7e3, release=0.05e3)
            fileName = str(variation) + str(order) + ".wav"
            path = str(filePath) + '/' + fileName
            sig.export(path)