import src.main.ValConstants as vc
import src.main.Note as Note

"""
Miscellaneous util functions for the Valerie sound design project.
"""

def interval(note1, note2):
    """
    Returns the distance in semitones between the two given notes.
    Negative values indicate a drop in pitch.
    :param note1: Starting note. Must be a valid Note object
    whose pitch is within the range C-1 - G9
    :param note2: Note to approach.
    :return: The distance in semitones between
    note1 and note2.
    """
    n1IsNote = isinstance(note1,Note.Note)
    n2IsNote = isinstance(note2,Note.Note)
    if (not n1IsNote or not n2IsNote):
        raise TypeError("Please input two Note objects.")
    else:
        n1MIDI = note1.getMIDI()
        n2MIDI = note2.getMIDI()
        if (n1MIDI > vc.MIDIMAX or n1MIDI < vc.MIDIMIN):
            raise Exception("Starting note is an unrecognized note name.")
        elif (n2MIDI > vc.MIDIMAX or n2MIDI < vc.MIDIMIN):
            raise Exception("Approach note is an unrecognized note name.")
        else:
            return note2.getMIDI() - note1.getMIDI()

def validateNoteName(noteName):
    """
    Checks whether the given note name is recognized by
    this system. Recognized note names are within 12-TET
    and have no more than one accidental.
    :param noteName: Note name to check for validity.
    :return: True if the given note name is valid, false otherwise.
    """
    i = 0
    found = False
    notesLength = len(vc.NOTES)
    while (not found) and (i < notesLength):
        item = vc.NOTES[i]
        isTuple = isinstance(item, tuple)
        if isTuple:
            if noteName in item:
                found = True
                return True
        else:
            if noteName == item:
                found = True
                return True
        i += 1
    # If we've reached this point, the given note name is not valid.
    return False

def MIDIFromNote(noteName,octave):
    """
    Gets the MIDI number associated with the given note.
    :param noteName: Note name to get MIDI number of, as a
    string. Cannot have more than one accidental.
    Ex. "A", "Bb", "C#"
    :param octave: Octave of the given note as an integer
    between the lower and upper bound of valid octaves
    expressed in ValConstants.OCTAVES.
    :return: An integer between 0-127, or -1 if the
    given note is not recognized
    """
    i = 0
    found = False
    notesLength = len(vc.NOTES)
    while (not found) and (i < notesLength):
        item = vc.NOTES[i]
        isTuple = isinstance(item, tuple)
        if isTuple:
            if noteName in item:
                found = True
                return i + (12 * (1 + octave))
        else:
            if noteName == item:
                found = True
                return i + (12 * (1 + octave))
        i += 1
    # If we've reached this point, the given note name is not valid.
    return -1
