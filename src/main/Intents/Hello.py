'''
Model of the speech intent 'hello'.
'''
import src.main.ValConstants as vc
import src.main.ValUtil as vu
from src.main.Intents.Intent import Intent
class Hello(Intent):

    def __init__(self):
        super().__init__()
        self.centralNote = "D"
        self.centralOctave = 5
        self.pitchRange = 9
        self.mode = vc.IONIAN
        self.contour = vc.BOTH
        self.tempo = vc.FAST
        self.rhythm = [vc.HALFSTEP, vc.HALFSTEP]
        self.length = 2
        self.key = "D"
        self.interval = vc.MAJ3RD
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