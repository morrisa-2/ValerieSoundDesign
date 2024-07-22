'''
Model of the speech intent 'thank you'.
'''
import src.main.ValConstants as v
from src.main.Intents.Intent import Intent

class ThankYou(Intent):
    def __init__(self):
        super().__init__()
        self.centralNote = "A#5"
        self.pitchRange = 9
        self.mode = v.IONIAN
        self.contour = v.DESCENDING
        self.tempo = v.SLOW
        self.rhythm = [v.LONG,v.SHORT, v.LONG]
        self.length = 3
        self.key = "A#"
        self.interval = v.MAJ2ND