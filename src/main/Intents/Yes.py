'''
Model of the speech intent 'yes'.
'''
import src.main.ValConstants as vc
import src.main.ValUtil as vu
from src.main.Intents.Intent import Intent

class Yes(Intent):
    def __init__(self):
        super().__init__()
        self.centralNote = "G"
        self.centralOctave = 5
        self.pitchRange = 5
        self.mode = vc.IONIAN
        self.contour = vc.ASCENDING
        self.tempo = vc.FAST
        self.rhythm = [vc.EIGHTH, vc.HALFSTEP]
        self.length = 2
        self.key = "G"
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