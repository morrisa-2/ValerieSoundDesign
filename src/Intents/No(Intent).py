'''
Model of the speech intent 'no'.
'''
import src.ValConstants as v
import Intent

class No(Intent):
    def __init__(self):
        self.setCentralNote(["G3","F#3"])
        self.setPitchRange(7)
        self.setMode(v.AEOLIAN)
        self.setContour(v.DESCENDING)
        self.setTempo(v.FAST)
        self.setRhythm([v.SHORT,v.SHORT,v.LONG])
        self.setLength(3)
        self.setKey("C")
        self.setInterval(v.MIN2ND)