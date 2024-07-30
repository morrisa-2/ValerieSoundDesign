'''
A set of musical shorthands for use in programming Valerie's
sound design engine.
'''

# STEPS
WHOLE = 2
HALF = 1

# MODES
IONIAN = [WHOLE,WHOLE,HALF,WHOLE,WHOLE,WHOLE,HALF]
DORIAN = [WHOLE,HALF,WHOLE,WHOLE,WHOLE,HALF,WHOLE]
PHRYGIAN = [HALF,WHOLE,WHOLE,WHOLE,HALF,WHOLE,WHOLE]
LYDIAN = [WHOLE,WHOLE,WHOLE,HALF,WHOLE,WHOLE,HALF]
MIXOLYDIAN = [WHOLE,WHOLE,HALF,WHOLE,WHOLE,HALF,WHOLE]
AEOLIAN = [WHOLE,HALF,WHOLE,WHOLE,HALF,WHOLE,WHOLE]
LOCRIAN = [HALF,WHOLE,WHOLE,HALF,WHOLE,WHOLE,WHOLE]

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
SHORT = 0.5
MID = 1
LONG = 2

# DIRECTIONAL DESCRIPTORS
ASCENDING = "ASCENDING"
DESCENDING = "DESCENDING"
BOTH = "BOTH"
CONSTANT = "CONSTANT"

# TEMPO - Measured in seconds per quarter note.
# Does this make any sense? Why am I doing it this way????
# TODO: Check how to format tempo.
SLOW = 1
MODERATE = 0.5
FAST = 0.25

# TODO: Make a Note class?
# NOTES - No enharmonic spellings, sharps prioritized
NOTES = ["C0","C#0","D0","D#0","E0","F0","F#0","G0","G#0","A0","A#0","B0",
         "C1","C#1","D1","D#1","E1","F1","F#1","G1","G#1","A1","A#1","B1",
         "C2","C#2","D2","D#2","E2","F2","F#2","G2","G#2","A2","A#2","B2",
         "C3","C#3","D3","D#3","E3","F3","F#3","G3","G#3","A3","A#3","B3",
         "C4","C#4","D4","D#4","E4","F4","F#4","G4","G#4","A4","A#4","B4",
         "C5","C#5","D5","D#5","E5","F5","F#5","G5","G#5","A5","A#5","B5",
         "C6","C#6","D6","D#6","E6","F6","F#6","G6","G#6","A6","A#6","B6",
         "C7","C#7","D7","D#7","E7","F7","F#7","G7","G#7","A7","A#7","B7",
         "C8","C#8","D8","D#8","E8","F8","F#8","G8","G#8","A8","A#8","B8",
         "C9","C#9","D9","D#9","E9","F9","F#9","G9"]

# DEFAULTS
DEFAULT_CENTER = "C4"
DEFAULT_RANGE = 7
DEFAULT_MODE = IONIAN
DEFAULT_CONTOUR = BOTH
DEFAULT_TEMPO = MODERATE
DEFAULT_RHYTHM = [SHORT,SHORT,LONG]
DEFAULT_LENGTH = 3
DEFAULT_KEY = "C"
DEFAULT_INTERVAL = P5
