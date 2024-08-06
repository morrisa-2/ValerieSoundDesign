'''
Model of the speech intent 'alert'.
'''
import src.main.ValConstants as v
from src.main.Intents.Intent import Intent

class Alert(Intent):
    def __init__(self):
        super().__init__()
        self.centralNote = "F#"
        self.centralOctave = 7
        self.pitchRange = 11
        self.mode = v.LYDIAN
        self.contour = v.DESCENDING
        self.tempo = v.MODERATE
        self.rhythm = [v.HALFSTEP, v.HALFSTEP]
        self.length = 2
        self.key = "C"
        self.interval = v.TRI

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