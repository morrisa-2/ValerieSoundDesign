"""
Connection between Python and SuperCollider using
the SCAMP and pythonosc modules.
"""

from pythonosc.udp_client import SimpleUDPClient
import src.main.Python.Model.Variation as Variation

class SCConnection:

    def __init__(self):
        # Right now this is just the default input port--
        # maybe there's a way to get SC to communicate this directly?
        port = 57120
        ip = "127.0.0.1"
        self.client = SimpleUDPClient(ip,port)

    def initialize(self):
        """
        Sends a message to the SuperCollider synth to initialize the SynthDef.
        """
        # Could add more parameters for python-side customizability (?)
        self.client.send_message("/initialize",True)

    def _generateSignal(self,variation):
        """
        Plays the given variation through the SuperCollider synth.
        :param variation: Variation to generate a signal for.
        """
        if not (isinstance(variation, Variation.Variation)):
            raise TypeError("Variation argument must be a Variation object.")
        else:
            # This will be a tuple of frequencies.
            pitches = variation.getFrequencies()
            # This will be a tuple of note lengths.
            rhythm = variation.getRhythm()
            tempo = variation.getTempo()

            self.client.send_message("/tempo", tempo)
            self.client.send_message("/pitches",pitches)
            self.client.send_message("/rhythm",rhythm)
            self.client.send_message("/generate",True)
            self.client.send_message("/debug",True)


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