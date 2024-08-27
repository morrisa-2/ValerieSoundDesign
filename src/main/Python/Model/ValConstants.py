'''
A set of musical shorthands for use in programming Valerie's
sound design engine.
'''

# STEPS
WHOLESTEP = 2
HALFSTEP = 1

# MODES
IONIAN = [WHOLESTEP, WHOLESTEP, HALFSTEP, WHOLESTEP, WHOLESTEP, WHOLESTEP, HALFSTEP]
DORIAN = [WHOLESTEP, HALFSTEP, WHOLESTEP, WHOLESTEP, WHOLESTEP, HALFSTEP, WHOLESTEP]
PHRYGIAN = [HALFSTEP, WHOLESTEP, WHOLESTEP, WHOLESTEP, HALFSTEP, WHOLESTEP, WHOLESTEP]
LYDIAN = [WHOLESTEP, WHOLESTEP, WHOLESTEP, HALFSTEP, WHOLESTEP, WHOLESTEP, HALFSTEP]
MIXOLYDIAN = [WHOLESTEP, WHOLESTEP, HALFSTEP, WHOLESTEP, WHOLESTEP, HALFSTEP, WHOLESTEP]
AEOLIAN = [WHOLESTEP, HALFSTEP, WHOLESTEP, WHOLESTEP, HALFSTEP, WHOLESTEP, WHOLESTEP]
LOCRIAN = [HALFSTEP, WHOLESTEP, WHOLESTEP, HALFSTEP, WHOLESTEP, WHOLESTEP, WHOLESTEP]

# INTERVALS
MIN2ND = 1
MAJ2ND = 2
MIN3RD = 3
MAJ3RD = 4
P4 = 5
TRI = 6
P5 = 7
MIN6TH = 8
MAJ6TH = 9
MIN7TH = 10
MAJ7TH = 11
OCT = 12

# RHYTHMIC DESCRIPTORS
EIGHTH = 0.5
QUARTER = 1
HALF = 2

# DIRECTIONAL DESCRIPTORS
ASCENDING = "ASCENDING"
DESCENDING = "DESCENDING"
BOTH = "BOTH"
CONSTANT = "CONSTANT"

# TEMPO - Measured in BPM.
SLOW = 150
MODERATE = 200
FAST = 300

# NOTES
NOTES = (("B#","C"),("C#","Db"),"D",("D#","Eb"),
         ("E","Fb"),("E#","F"),("F#","Gb"),"G",
         ("G#","Ab"),"A",("A#","Bb"),("B","Cb"))

# CIRCLE OF FIFTHS - Rudimentary, just for determining what notes to take for what keys.
RIGHT_OF_C = ("G","D","A","E","B","F#")
LEFT_OF_C = ("F","Bb","Eb","Ab","Db","Gb")

# OCTAVE - Range encompasses all MIDI notes
OCTAVES = (-1,9)

# MIDI RANGE
MIDIMAX = 127
MIDIMIN = 0

# RHYTHM POOL - Sucks to have this hard-coded :(
RHYTHM_POOL = [[EIGHTH, EIGHTH, HALF],[QUARTER,EIGHTH,QUARTER]]

# DEFAULTS
DEFAULT_CENTER = "C"
DEFAULT_OCTAVE = 4
DEFAULT_RANGE = 7
DEFAULT_MODE = IONIAN
DEFAULT_CONTOUR = BOTH
DEFAULT_TEMPO = MODERATE
DEFAULT_RHYTHM = [EIGHTH, EIGHTH, HALF]
DEFAULT_LENGTH = 3
DEFAULT_KEY = "C"
DEFAULT_INTERVAL = P5
