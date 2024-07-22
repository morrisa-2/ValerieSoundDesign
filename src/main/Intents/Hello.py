'''
Model of the speech intent 'hello'.
'''
import src.main.ValConstants as v
from src.main.Intents.Intent import Intent
class Hello(Intent):
    print("Hello loaded")
    print(__file__)
    def __init__(self):
        super().__init__()
        self.centralNote = "D5"
        self.pitchRange = 9
        self.mode = v.IONIAN
        self.contour = v.BOTH
        self.tempo = v.FAST
        self.rhythm = [v.LONG,v.LONG]
        self.length = 2
        self.key = "D"
        self.interval = v.MAJ3RD

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