import src.main.ValConstants  as v

"""
Miscellaneous util functions for the Valerie sound design project.
"""

def interval(note1, note2):
    """
    Returns the distance in semitones
    between the two given notes. Negative values
    indicate a drop in pitch.
    :param note1: Starting note.
    :param note2: Note to approach.
    :return: The distance in semitones between
    note1 and note2.
    """
    note1Index = v.NOTES.index(note1)
    if (note1Index < 0):
        raise IndexError("note1 out of range.")
    note2Index = v.NOTES.index(note2)
    if (note2Index < 0):
        raise IndexError("note2 out of range.")
    return note2Index - note1Index

