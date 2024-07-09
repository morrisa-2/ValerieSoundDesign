'''
Model of the speech intent 'thank you'.
'''
import src.ValConstants as v
import Intent

class ThankYou(Intent):
    def __init__(self):
        self.setCentralNote([v.NOTES.index("A#3"),v.NOTES.index("D4")])
        self.setPitchRange(9)
        self.setMode(v.IONIAN)
        self.setContour(v.DESCENDING)
        self.setTempo(v.SLOW)
        self.setRhythm([v.LONG,v.SHORT, v.LONG])
        self.setLength(3)
        self.setKey("A#")
        self.setInterval(v.MAJ2ND)