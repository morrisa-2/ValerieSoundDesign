'''
Model of the speech intent 'goodbye'.
'''
import src.main.ValConstants as v
from src.main.Intents.Intent import Intent

class Goodbye(Intent):
    def __init__(self):
        super().__init__()
        self.centralNote = "F#3"
        self.pitchRange = 8
        self.mode = v.IONIAN
        self.contour = v.DESCENDING
        self.tempo = v.SLOW
        self.rhythm = [v.SHORT,v.SHORT,v.LONG]
        self.length = 3
        self.key = "D"
        self.interval = v.P4

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