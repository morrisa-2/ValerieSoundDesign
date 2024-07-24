"""
A simple synth patch for the gensound module.
"""

from gensound import Sine, Gain, ADSR, FadeIn, FadeOut
from gensound.filters import SimpleBandPass
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

    def _generateSignal(self,variation):
        """
        Returns a gensound Signal object that corresponds
        to the given Variation.
        :param variation: Variation to generate a signal for.
        :return: Signal that is represented by the given variation.
        """
        # Returns a tuple consisting of the variation's notes and tempo.
        unpackedVariation = variation.prepForSignal()

        # Transforms are kind of busted for right now...
        # TODO: Fix ADSR amplitude glitch.
        # envelope = ADSR(attack=0.05e3, decay=0.02e3, sustain=0.7e3, release=0.1e3)
        gain = Gain(-4)
        # TODO: Fix fades glitch (??)
        # fades = FadeOut(duration=0.1e3) * FadeIn(duration=0.1e3)
        # bandpass = SimpleBandPass(lower=100, upper=10000)

        sig = Sine(unpackedVariation[0], duration=unpackedVariation[1])
        sig = sig * gain
        return sig

    def exportVariation(self, variation, order, filePath):
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
            sig = self._generateSignal(variation)
            fileName = str(variation) + str(order) + ".wav"
            path = str(filePath) + '/' + fileName
            sig.export(path)