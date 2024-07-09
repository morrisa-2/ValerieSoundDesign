'''
Model of the speech intent 'goodbye'.
'''
import src.ValConstants as v
import Intent

class Goodbye(Intent):
    def __init__(self):
        self.setCentralNote("F#3")
        self.setPitchRange(8)
        self.setMode(v.IONIAN)
        self.setContour(v.DESCENDING)
        self.setTempo(v.SLOW)
        self.setRhythm([v.SHORT,v.SHORT,v.LONG])
        self.setLength(3)
        self.setKey("D")
        self.setInterval(v.P4)