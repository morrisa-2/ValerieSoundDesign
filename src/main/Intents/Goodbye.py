'''
Model of the speech intent 'goodbye'.
'''
import src.main.ValConstants as vc
import src.main.ValUtil as vu
from src.main.Rhythm import Rhythm
from src.main.Intents.Intent import Intent

class Goodbye(Intent):
    def __init__(self):
        super().__init__()
        self.centralNote = "F#"
        self.centralOctave = 5
        self.pitchRange = 8
        self.mode = vc.IONIAN
        self.contour = vc.DESCENDING
        self.tempo = vc.SLOW
        self.rhythm = Rhythm([vc.EIGHTH, vc.EIGHTH, vc.HALF])
        self.length = 3
        self.key = "D"
        self.interval = vc.P4
        vu.addRhythmToPool(self.rhythm)

    def getCentralNote(self):
        return super().getCentralNote()
    def getPitchRange(self):
        return super().getPitchRange()
    def getMode(self):
        return super().getMode()
    def getContour(self):
        return super().getContour()
    def getTempo(self):
        return super().getTempo()
    def getRhythm(self):
        return super().getRhythm()
    def getLength(self):
        return super().getLength()
    def getKey(self):
        return super().getKey()
    def getInterval(self):
        return super().getInterval()