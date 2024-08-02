"""
Connection between Python and SuperCollider using
the SCAMP and pythonosc modules.
"""

from scamp import *
from pathlib import Path
import expenvelope.envelope
from pythonosc.udp_client import SimpleUDPClient

class SCConnection:

    def __init__(self,clock):
        self.s = Session()
        # Right now this is just the default input port--
        # maybe there's a way to get SC to communicate this directly?
        port = 57120
        ip = "127.0.0.1"
        self.client = SimpleUDPClient(ip,port)
        self.synth = self.s.new_osc_part("Valerie",port=port)
        # TODO: Check if this is a Clock object.
        self.clock = clock

    def _generateSignal(self,variation):
        """
        Plays the given variation through the SuperCollider synth.
        :param variation: Variation to generate a signal for.
        """
        # TODO: Reformat variation contents
        # This will be an array of indices which match up w/MIDI note numbers.
        pitches = variation.getMIDINotes()
        env = expenvelope.Envelope
        # This will be an array of note lengths.
        rhythm = variation.getRhythm()
        i = 0
        for note in pitches:
            lastNote = i == (len(pitches) - 1)
            # Removing the envelope for now just to simplify
            # env = env.adsr(attack_length=0.1, attack_level=1, decay_length=0, sustain_level=1, sustain_length=rhythm[i], release_length=0.1)
            if not lastNote:
                nextNote = pitches[i + 1]
                self.synth.play_note(pitch=[note,nextNote],volume=0.5,length=rhythm[i], clock=self.clock)
            else:
                self.synth.play_note(pitch=note, volume=0.5, length=rhythm[i], clock=self.clock)
            i += 1

    def exportVariation(self, variation, ordinal, filepath):
        """
        Exports the given variation as a wav file.
        :param variation: Variation to play.
        :param ordinal: Number to be appended to the end of the
        exported file's name to avoid accidental overwriting.
        :param filepath: String representing the directory in which
        this variation is to be exported.
        """

        fileName = variation.nameOfIntent() + str(ordinal) + ".wav"
        file = filepath + fileName

        duration = variation.lengthInSeconds()

        self.client.send_message("/filepath",file)
        self.client.send_message("/duration",duration)

        # Passing True into /record starts a recording for the given
        # duration at the given filepath. Passing in false stops the
        # recording immediately, or does nothing if no recording is
        # currently being made.
        self.client.send_message("/record",True)

        self._generateSignal(variation)