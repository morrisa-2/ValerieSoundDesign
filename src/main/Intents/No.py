'''
Model of the speech intent 'no'.
'''
import src.main.ValConstants as v
from src.main.Intents.Intent import Intent

class No(Intent):
    def __init__(self):
        super().__init__()
        self.centralNote = "F#"
        self.centralOctave = 5
        self.pitchRange = 7
        self.mode = v.AEOLIAN
        self.contour = v.DESCENDING
        self.tempo = v.FAST
        self.rhythm =  [v.EIGHTH, v.EIGHTH, v.HALF]
        self.length = 3
        self.key = "C"
        self.interval = v.MIN2ND