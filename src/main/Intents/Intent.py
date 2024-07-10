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

import src.main.ValConstants as v

class Intent:
    # Defaults

    # Instance vars
    def __init__(self):
        self.centralNote = v.DEFAULT_CENTER
        self.pitchRange = v.DEFAULT_RANGE
        self.mode = v.DEFAULT_MODE
        self.contour = v.DEFAULT_CONTOUR
        self.tempo = v.DEFAULT_TEMPO
        self.rhythm = v.DEFAULT_RHYTHM
        self.length = v.DEFAULT_LENGTH
        self.key = v.DEFAULT_KEY
        self.interval = v.DEFAULT_INTERVAL

    # Getters
    def getCentralNote(self):
        return self.centralNote
    def getPitchRange(self):
        return self.pitchRange
    def getMode(self):
        return self.mode
    def getContour(self):
        return self.contour
    def getTempo(self):
        return self.tempo
    def getRhythm(self):
        return self.rhythm
    def getLength(self):
        return self.length
    def getKey(self):
        return self.key
    def getInterval(self):
        return self.interval

    # Setters
    def setCentralNote(self,note):
        self.centralNote = note
    def setPitchRange(self,range):
        self.pitchRange = range
    def setMode(self,mode):
        self.mode = mode
    def setContour(self,contour):
        self.contour = contour
    def setTempo(self,tempo):
        self.tempo = tempo
    def setRhythm(self,rhythm):
        self.rhythm = rhythm
    def setLength(self,length):
        self.length = length
    def setKey(self,key):
        self.key = key
    def setInterval(self,interval):
        self.interval = interval
        