'''
Model of the speech intent 'hello'.
'''
import src.main.ValConstants as v
import Intent
class Hello(Intent):
    def __init__(self):
        self.setCentralNote(v.NOTES.index("D4"))
        self.setPitchRange(9)
        self.setMode(v.IONIAN)
        self.setContour(v.BOTH)
        self.setTempo(v.FAST)
        self.setRhythm([v.LONG,v.LONG])
        self.setLength(2)
        self.setKey("D")
        self.setInterval(v.MAJ3RD)