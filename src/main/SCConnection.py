"""
Connection between Python and SuperCollider using
the SCAMP and pythonosc modules.
"""

from scamp import *
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
        env = Envelope()
        # This will be an array of note lengths.
        rhythm = variation.getRhythm()
        i = 0
        for note in pitches:
            lastNote = i == (len(pitches) - 1)
            nextNote = pitches[i+1]
            if not lastNote:
                self.synth.play_note([note,nextNote],env,rhythm[i])
            else:
                self.synth.play_note(note, env, rhythm[i])
            i += 1

    def exportVariation(self, variation):
        """
        Exports the given variation as a wav file.
        :param variation: Variation to play.
        """
        self.client.send_message("/recording/start")
        self._generateSignal(variation)
        self.client.send_message("/recording/end")

        # pathIsString = isinstance(filePath,str)
        # if pathIsString:
        #     filePath = Path(filePath)
        # if not filePath.exists():
        #     raise NameError("Please enter an existing path.")
        # if not filePath.is_dir():
        #     raise TypeError("Please enter a path to a directory.")
        # else:
        #     sig = self._generateSignal(variation)
        #     fileName = str(variation) + str(order) + ".wav"
        #     path = str(filePath) + '/' + fileName
        #     sig.export(path)