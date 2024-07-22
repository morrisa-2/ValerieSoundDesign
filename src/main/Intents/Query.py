'''
Model of the speech intent 'query'.
'''
import src.main.ValConstants as v
from src.main.Intents.Intent import Intent

class Query(Intent):
    def __init__(self):
        super().__init__()
        self.centralNote = "C#4"
        self.pitchRange = 9
        self.mode = v.AEOLIAN
        self.contour = v.ASCENDING
        self.tempo = v.FAST
        self.rhythm = [v.SHORT, v.LONG]
        self.length = 2
        self.key = "E"
        self.interval = v.MAJ2ND