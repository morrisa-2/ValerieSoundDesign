'''
Models one of Valerie's speech intents.
Brief explanation of qualities:
* Central Note  Note which must be present in all variations of
                this intent. This note does not have to be the key
                center of the intent, but must be within the key.
* Pitch Range   Range of semitones around the central note that each
                note can fall within. For instance, an intent whose
                central pitch is C5 and whose range is 7 semitones can
                select notes between F4 and G5. One can also provide
                separate values for lower and upper bounds of the range
                as a list of two integers [+,-]
* Mode          The modality this intent occupies.
* Contour       The shape of this intent's pitch contour. Classified as
                ascending, descending, both, or constant. Note that this
                selection is not exclusive--an intent which has an ascending
                contour does not necessarily contain only ascending intervals,
                but does place more weight on ascension and must end at a higher
                pitch than the central note. The inverse is true of descent.
* Tempo         The speed of this intent. This is a qualitative description
                which only refers to slow, moderate, and fast.
* Rhythm        Informal description of intent's rhythm. This rhythm is
                described as a list of note lengths--short, mid, and long.
                For instance, an intent might have the rhythm [short, short, long].
* Length        An intent's length in number of notes. Note that this does not
                is not constrained to the rhythm of the intent. If an intent
                is longer than its rhythmic pattern, it will simply wrap around
                to the beginning of the pattern.
* Key           Key center of the intent.
* Interval      The interval that must be present in each variation of this intent.
                The direction of this interval must adhere to the contour
                of the intent. For instance, if the intent is ascending and
                must contain a perfect 5th, that perfect 5th must also be
                ascending.
'''

import src.main.Python.Model.ValUtil as vu
import src.main.Python.Model.ValConstants as vc
from src.main.Python.Controllers.DBConnection import DBConnection
from src.main.Python.Model.Modality import Modality, Modes
from src.main.Python.Model.Pitch import Pitch
from src.main.Python.Model.Rhythm import Rhythm
from src.main.Python.Model.Contour import Contour

class Intent:
    # Instance vars
    def __init__(self,name):
        """
        Non-default constructor.
        :param name: Name of intent to model. Name must
        already be present in the database.
        """
        if name == "test":
            self._setForTest()
        else:
            validName = DBConnection.validateIntent(name)
            if not validName:
                raise ValueError("The given intent does not exist.")
            else:
                # Gets a dictionary of info from the DB
                info = DBConnection.getIntentInfo(name)

                # Assigns info fetched from DB
                self.name = info["intentName"]

                centralNote = info["centralNote"]
                centralOctave = info["centralOctave"]
                self.centralPitch = Pitch(centralNote,centralOctave)

                self.pitchRange = info["pitchRange"]

                modeName = info["modality"].upper()
                for enum in Modes:
                    if modeName in str(enum):
                        self.modality = Modality(enum)

                if self.modality == None:
                    raise Exception("Unrecognized modality.")

                # DB stores as string; check values of enum in Contour.
                contourInfo = info["contour"]

                for enum in Contour:
                    if enum.value == contourInfo:
                        self.contour = enum

                # If self.contour hasn't been populated yet, the string
                # from the DB is not recognized by Contour.
                if self.contour == None:
                    raise Exception("Unrecognized contour.")

                self.tempo = info["tempo"]
                self.keyCenter = info["keyCenter"]
                self.centralInterval = info["centralInterval"]

                # Gets a dictionary of rhythm info from the DB
                rhythmInfo = DBConnection.getRhythmByIntent(name)

                # Assigns rhythm info fetched from DB
                self.rhythmLength = rhythmInfo["rhythmLength"]

                durations = []
                for i in range(self.rhythmLength):
                    toAdd = rhythmInfo["dur{num}".format(num=i)]
                    durations.append(toAdd)

                rhythm = Rhythm(self.name,durations)

                self.rhythm = rhythm

    def _setForTest(self):
        """
        Manually sets up an intent for testing
        without the database.
        """
        self.name = "test"
        self.centralPitch = Pitch("C", 5)
        self.pitchRange = 12
        self.modality = vc.IONIAN
        self.contour = Contour.ASCENDING
        self.tempo = 100
        self.keyCenter = "C"
        self.centralInterval = 5
        durations = [1, 1]
        self.rhythm = Rhythm(self.name,durations)
        self.rhythmLength = len(durations)

    # Getters
    def getCentralPitch(self):
        return self.centralPitch
    def getCentralNote(self):
        return self.centralPitch.getName()
    def getCentralOctave(self):
        return self.centralPitch.getOctave()
    def getPitchRange(self):
        return self.pitchRange
    def getMode(self):
        return self.modality
    def getContour(self):
        return self.contour
    def getTempo(self):
        return self.tempo
    def getRhythm(self):
        return self.rhythm
    def getLength(self):
        return self.rhythmLength
    def getKey(self):
        return self.keyCenter
    def getInterval(self):
        return self.centralInterval

    def __str__(self):
        """
        Returns a string representation of this
        intent.
        :return: A string representing this intent.
        Ex. "Hello"
        """
        return self.name

    def getAvailablePitches(self):
        """
        Gets a tuple of all the pitches that this intent
        can play.
        :return: A tuple containing Note objects that
        represent this Intent's range of available pitches.
        """
        return vu.getPitches(self)
