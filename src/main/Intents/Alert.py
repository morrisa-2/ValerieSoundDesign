'''
Model of the speech intent 'alert'.
'''
import src.main.ValConstants as v
import Intent


class Alert(Intent):
    def __init__(self):
        self.setCentralNote(v.NOTES.index("F#7"))
        self.setPitchRange(11)
        self.setMode(v.LYDIAN)
        self.setContour(v.DESCENDING)
        self.setTempo(v.MODERATE)
        self.setRhythm([v.LONG, v.LONG])
        self.setLength(2)
        self.setKey("C")
        self.setInterval(v.TRI)
