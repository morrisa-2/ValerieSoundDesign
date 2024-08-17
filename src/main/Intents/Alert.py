'''
Model of the speech intent 'alert'.
'''
import src.main.ValConstants as vc
import src.main.ValUtil as vu
from src.main.Rhythm import Rhythm
from src.main.Intents.Intent import Intent

class Alert(Intent):
    def __init__(self):
        super().__init__()
        self.centralNote = "F#"
        self.centralOctave = 7
        self.pitchRange = 11
        self.mode = vc.LYDIAN
        self.contour = vc.DESCENDING
        self.tempo = vc.MODERATE
        self.rhythm = Rhythm([vc.HALFSTEP, vc.HALFSTEP])
        self.length = 2
        self.key = "C"
        self.interval = vc.TRI
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