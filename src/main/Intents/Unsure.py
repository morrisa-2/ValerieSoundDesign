'''
Model of the speech intent 'unsure'.
'''
import src.main.ValConstants as v
import Intent

class Unsure(Intent):
    def __init__(self):
        self.setCentralNote([v.NOTES.index("G#3"),v.NOTES.index("F3")])
        self.setPitchRange(9)
        self.setMode(v.AEOLIAN)
        self.setContour(v.BOTH)
        self.setTempo(v.MODERATE)
        self.setRhythm([v.LONG,v.SHORT, v.LONG])
        self.setLength(3)
        self.setKey("F")
        self.setInterval(v.MIN3RD)