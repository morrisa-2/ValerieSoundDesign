"""
Connection between Python and SuperCollider using
the SCAMP and pythonosc modules.
"""

from scamp import *
from pathlib import Path
import expenvelope.envelope
import rtmidi
from pythonosc.udp_client import SimpleUDPClient

class SCConnection:

    def __init__(self):
        self.s = Session()
        # Right now this is just the default input port--
        # maybe there's a way to get SC to communicate this directly?
        port = 57120
        ip = "127.0.0.1"
        self.client = SimpleUDPClient(ip,port)
        self.synth = self.s.new_osc_part("Valerie",port=port)

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
            env = env.adsr(attack_length=0.1, attack_level=1, decay_length=0,
                           sustain_level=1, sustain_length=rhythm[i], release_length=0.1)
            if not lastNote:
                nextNote = pitches[i + 1]
                self.synth.play_note([note,nextNote],env,rhythm[i])
            else:
                self.synth.play_note(note, env, rhythm[i])
            i += 1

    def exportVariation(self, variation, ordinal, filepath):
        """
        Exports the given variation as a wav file.
        :param variation: Variation to play.
        :param ordinal: Number to be appended to the end of the
        exported file's name to avoid accidental overwriting.
        :param filepath: Path object or string representing the directory in which
        this variation is to be exported.
        """
        if (isinstance(filepath,str)):
            filepath = Path(filepath)

        if (not filepath.exists()):
            print("Creating directory at the given filepath...")
            filepath.mkdir()
        elif (not filepath.is_dir()):
            raise TypeError("Please input a path to a directory.")

        fileName = variation.nameOfIntent() + str(ordinal) + ".wav"
        filepath = str(filepath)
        file = filepath + fileName

        duration = variation.lengthInSeconds()

        self.client.send_message("/recording/start",[file,duration])
        self._generateSignal(variation)
        self.client.send_message("/recording/end",0)