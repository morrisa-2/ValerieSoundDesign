'''
Model of the speech intent 'yes'.
'''
import src.main.ValConstants as v
from src.main.Intents.Intent import Intent

class Yes(Intent):
    def __init__(self):
        super().__init__()
        self.centralNote = "G5"
        self.pitchRange = 5
        self.mode = v.IONIAN
        self.contour = v.ASCENDING
        self.tempo = v.FAST
        self.rhythm = [v.SHORT,v.LONG]
        self.length = 2
        self.key = "G"
        self.interval = v.P4