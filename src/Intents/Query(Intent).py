'''
Model of the speech intent 'query'.
'''
import src.ValConstants as v

def __init__(self):
    self.setCentralNote("C#4")
    self.setPitchRange(9)
    self.setMode(v.AEOLIAN)
    self.setContour(v.ASCENDING)
    self.setTempo(v.FAST)
    self.setRhythm([v.SHORT, v.LONG])
    self.setLength(2)
    self.setKey("E")
    self.setInterval(v.MAJ2ND)