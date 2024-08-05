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
    n1IsNote = note1.isinstance(Note.Note)
    n2IsNote = note2.isinstance(Note.Note)
    if (not n1IsNote or not n2IsNote):
        raise TypeError("Please input two Note objects.")
    else:
        n1MIDI = note1.getMIDI()
        n2MIDI = note2.getMIDI()
        if (n1MIDI > len(vc.NOTES) or n1MIDI < 0):
            raise Exception("Starting note is an unrecognized note name.")
        elif (n2MIDI > len(vc.NOTES) or n2MIDI < 0):
            raise Exception("Approach note is an unrecognized note name.")
        else:
            return note2.getMIDI() - note1.getMIDI()
