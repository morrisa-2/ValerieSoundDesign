import random

import src.main.Python.Model.ValConstants as vc
from src.main.Python.Model.Rhythm import Rhythm
from src.main.Python.Model.Pitch import Pitch
from src.main.Python.Model.Intent import Intent

from src.main.Python.Controllers.DBConnection import DBConnection

"""
Handles all interactions between elements of ValConstants and
the rest of the classes in this project.
"""

def interval(pitch1, pitch2):
    """
    Returns the distance in semitones between the two given notes.
    Negative values indicate a drop in pitch.
    :param pitch1: Starting note. Must be a valid Note object
    whose pitch is within the range C-1 - G9
    :param pitch2: Note to approach.
    :return: The distance in semitones between
    note1 and note2.
    """
    isPitch1 = isinstance(pitch1, Pitch)
    isPitch2 = isinstance(pitch2, Pitch)
    if not (isPitch1 or isPitch2):
        raise TypeError("Please input two Pitch objects.")
    else:
        octave1 = pitch1.getOctave()
        octave2 = pitch2.getOctave()
        octDifference = octave2 - octave1

        # Relying on the indices feels kind of icky...
        index1 = _getNoteIndex(pitch1.getName(), vc.NOTES)
        index2 = _getNoteIndex(pitch2.getName(), vc.NOTES)
        indexDifference = index2 - index1

        return (12 * octDifference) + indexDifference

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

def MIDIFromPitch(name, octave):
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
            if name in item:
                found = True
                return i + (12 * (1 + octave))
        else:
            if name == item:
                found = True
                return i + (12 * (1 + octave))
        i += 1
    # If we've reached this point, the given note name is not valid.
    return -1

def _getNotesInRange(intent):
    """
    Gets a list of note names that expresses the given Intent's
    full range of notes to select from.
    This does not select by key, only by octave.
    :param intent: Intent to get the range of.
    :return: A list of note names in the given intent's range.
    """
    if not (isinstance(intent,Intent)):
        raise TypeError("Please input an Intent object.")
    else:
        toReturn = []
        pitchRange = intent.getPitchRange()
        centralNoteName = intent.getCentralNote()
        centralIndex = _getNoteIndex(centralNoteName,vc.NOTES)
        toReturn.append(vc.NOTES[centralIndex])
        increment = 0
        notesLen = len(vc.NOTES)
        for i in range(0,pitchRange):
            if (centralIndex + increment >= notesLen):
                increment = -centralIndex
            next = vc.NOTES[centralIndex + increment]
            toReturn.append(next)
        for i in range(-pitchRange,0):
            if (centralIndex - increment < 0):
                increment = notesLen - centralIndex - 1
            next = vc.NOTES[centralIndex + increment]
            toReturn.insert(0,next)
        return toReturn

def getPitches(intent):
    """
    Returns a tuple of Pitch objects that can be selected for
    Variations of the given Intent.
    :param intent: Intent to get the range of notes for.
    :return: A tuple of Pitch objects that express the given
    intent's range.
    """
    toReturn = []
    listOfNoteNames = _filterByKey(intent)
    listOfOctaves = _applyOctave(listOfNoteNames,intent)
    length = len(listOfNoteNames)
    for i in range(0,length):
        pitch = Pitch(name=listOfNoteNames[i], octave=listOfOctaves[i])
        toReturn.append(pitch)
    return tuple(toReturn)

def _applyOctave(listOfNoteNames,intent):
    """
    Applies the correct octave to the given list of
    note names based on the central note and octave
    of the given intent.
    :param listOfNoteNames: Collection of note names
    to apply octaves to.
    :param intent: Intent to base octave application off of.
    :return: A list of integers that correspond to the octave
    of each note name in listOfNoteNames.
    """
    toReturn = []
    centralNote = intent.getCentralNote()
    octave = intent.getCentralOctave()
    centralIndex = listOfNoteNames.index(centralNote)
    length = len(listOfNoteNames)

    for i in range(centralIndex,length):
        element = listOfNoteNames[i]
        if i > centralIndex and "C" in element:
            octave += 1
        toReturn.append(octave)

    octave = intent.getCentralOctave()

    for i in range(centralIndex-1,-1,-1):
        element = listOfNoteNames[i]
        if "B" in element:
            octave -= 1
        toReturn.insert(0,octave)

    return toReturn

def _filterByKey(intent):
    """
    Given a collection containing note names and tuples of note names,
    creates a new tuple of notes that adhere to the given intent's key.
    :param intent: Intent that this range is to be applied to.
    :return: A tuple of note names that are within the given intent's key.
    """
    keyCenter = intent.getKey()
    mode = intent.getMode()
    pitchRange = intent.getPitchRange()
    toReturn = []
    toReturn.append(keyCenter)
    counter = 0
    i = 0
    modeLen = len(mode)

    # Fill with all notes in key above key center.
    while counter < pitchRange:
        current = toReturn[-1]
        steps = mode[i]
        nextNote = _stepBy(steps,keyCenter,current)
        toReturn.append(nextNote)
        i += 1
        counter += steps
        if i >= modeLen:
            i = 0

    # Fill with all notes in key below key center.
    i = modeLen - 1
    counter = 0
    while counter < pitchRange:
        current = toReturn[0]
        steps = -mode[i]
        nextNote = _stepBy(steps,keyCenter,current)
        toReturn.insert(0,nextNote)
        i -= 1
        counter += -steps
        if i < 0:
            i = modeLen - 1

    return toReturn


def _stepBy(steps, key, startingNoteName):
    """
    Step through vc.NOTES by the given amount of semitones from the
    starting note and return the note within the given key at that position.
    This does not account for octaves.
    :param steps: Number of semitones to step by; negative integers indicate
    steps down from the starting note and vice versa.
    :param key: Key to filter notes by, as a note name on the circle of fifths.
    :param startingNoteName: Note name to step from.
    :return: The note name at the position n steps away from starting note
    in vc.NOTES where n = steps argument. This note name must be in the
    specified key.
    """
    startingIndex = _getNoteIndex(startingNoteName, vc.NOTES)
    if (startingIndex == -1):
        raise Exception("startingNote not in vc.NOTES.")
    else:
        notesLen = len(vc.NOTES)
        goTo = startingIndex + steps
        if (goTo >= notesLen):
            goTo = goTo - notesLen
        elif (goTo < 0):
            goTo = goTo + notesLen
        element = vc.NOTES[goTo]
        if (isinstance(element,tuple)):
            return _pickByKey(key,element)
        else:
            return element



def _pickByKey(key,toPickFrom):
    """
    Given a tuple of note names and a key,
    returns the note name that is in that key.
    :param key: Key to filter by.
    :param toPickFrom: Tuple of two note names,
    generally enharmonic spellings of the same pitch.
    :return: The note name which fits within the given key.
    """
    # Maybe there's a better way to do this?
    if key == "C#":
        return _takeSharp(toPickFrom)
    elif key == "Cb":
        return _takeFlat(toPickFrom)
    elif key == "C":
        return _takeNatural(toPickFrom)
    else:
        sharpKey = key in vc.RIGHT_OF_C
        flatKey = key in vc.LEFT_OF_C
        if not (flatKey or sharpKey):
            raise Exception("Unrecognized key.")
        else:
            natural = _takeNatural(toPickFrom)
            if natural != None:
                return natural
            else:
                if (sharpKey):
                    return _takeSharp(toPickFrom)
                else:
                    return _takeFlat(toPickFrom)

def _takeSharp(toPickFrom):
    """
    Given a tuple of two note names,
    returns the note that is sharp.
    :param toPickFrom: A tuple of two note names.
    :return: The note name that is sharp, or null
    if neither note name is sharp.
    """
    first = toPickFrom[0]
    second = toPickFrom[1]
    firstSharp = "#" in first
    secondSharp = "#" in second
    if firstSharp:
        return first
    elif secondSharp:
        return second
    else:
        return None

def _takeFlat(toPickFrom):
    """
    Given a tuple of two note names,
    returns the note that is flat.
    :param toPickFrom: A tuple of two note names.
    :return: The note name that is flat, or null
    if neither note name is flat.
    """
    first = toPickFrom[0]
    second = toPickFrom[1]
    firstFlat = "b" in first
    secondFlat = "b" in second
    if firstFlat:
        return first
    elif secondFlat:
        return second
    else:
        return None

def _takeNatural(toPickFrom):
    """
    Given a tuple of two note names,
    returns the note that is natural.
    :param toPickFrom: A tuple of two note names.
    :return: The note name that is natural, or null
    if neither note name is natural.
    """
    first = toPickFrom[0]
    second = toPickFrom[1]
    firstNatural = not ("b" in first or "#" in first)
    secondNatural = not ("b" in second or "#" in second)
    if firstNatural:
        return first
    elif secondNatural:
        return second
    else:
        return None

def _getNoteIndex(noteName:str, toIndex:list):
    """
    Helper function that gets the index of a note name in
    ValConstants. Note that this does not specify between
    enharmonic spellings of notes, and only selects the
    index of the tuple containing the given note name if it
    is not its own element.
    :param noteName: Name of note to get the index of.
    :param toIndex: List to get noteName's position in.
    :return: The index of either the given note name in the given
    collection, or the tuple containing it; -1 if the given note
    name is not in list.
    """
    i = 0
    found = False
    notesLength = len(toIndex)
    while (not found) and (i < notesLength):
        element = toIndex[i]
        if isinstance(element,tuple):
            if (noteName in element):
                return i
            else:
                i += 1
        else:
            if (noteName == element):
                return i
            else:
                i += 1
    # If we've reached this point, the given note name
    # is not in ValConstants' list of notes.
    return -1

def populateRhythmPool():
    """
    Populates the rhythm pool in ValConstants with all rhythms
    available in the database.
    """
    allDurs = DBConnection.getAllRhythms()
    items = allDurs.items()
    for item in items:
        toAdd = Rhythm(item[0],item[1])
        vc.RHYTHM_POOL.append(toAdd)

def addRhythmToPool(rhythm:Rhythm):
    """
    Adds the given rhythm to the available pool of
    rhythms for a variation to select from, as well as
    to the database. Cannot add duplicate rhythms.
    :param rhythm: Rhythm to add.
    :return: True if the given Rhythm was successfully added
    to the pool, false otherwise.
    """
    if not isinstance(rhythm, Rhythm):
        raise TypeError("Please input a Rhythm object.")
    else:
        pool = vc.RHYTHM_POOL
        if rhythm in pool:
            return False
        else:
            DBConnection.addRhythm(rhythm)
            pool.append(rhythm)
            return True

def pullRhythmFromPool():
    """
    Gets a random rhythm from the available pool of
    rhythms for a variation to select from.
    :return: A randomly selected rhythm.
    """
    pool = vc.RHYTHM_POOL
    return random.choice(pool)
