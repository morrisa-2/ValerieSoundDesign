'''
Model of the speech intent 'unsure'.
'''
import src.main.ValConstants as v
from src.main.Intents.Intent import Intent

class Unsure(Intent):
    def __init__(self):
        super().__init__()
        self.centralNote = "F5"
        self.pitchRange = 9
        self.mode = v.AEOLIAN
        self.contour = v.BOTH
        self.tempo = v.MODERATE
        self.rhythm = [v.LONG,v.SHORT, v.LONG]
        self.length = 3
        self.key = "F"
        self.interval = v.MIN3RD