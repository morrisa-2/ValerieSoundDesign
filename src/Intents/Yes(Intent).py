'''
Model of the speech intent 'yes'.
'''
import src.ValConstants as v
import Intent

class Yes(Intent):
    def __init__(self):
        self.setCentralNote("G3")
        self.setPitchRange(5)
        self.setMode(v.IONIAN)
        self.setContour(v.ASCENDING)
        self.setTempo(v.FAST)
        self.setRhythm([v.SHORT,v.LONG])
        self.setLength(2)
        self.setKey("G")
        self.setInterval(v.P4)