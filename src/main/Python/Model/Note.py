"""
Models a musical note. Has a duration expressed in
beats as well as a pitch expressed as frequency, note name,
and MIDI note number. Does not support microtonal adjustments
or tuning systems besides 12-TET. Can determine enharmonic
equivalence, but only supports single accidentals.
"""

import src.main.Python.Model.ValConstants as vc
import src.main.Python.Model.ValUtil as vu
from src.main.Python.Model.Pitch import Pitch
from typing import Self

class Note:

    def __init__(self, pitch, rhythVal:float):
        """
        Non-default constructor

        :param rhythVal: The number of beats this note should
        be played for as a float. Note that while there
        are constants for more common durations such as a quarter
        or eighth note, any numeric value will suffice.
        """
        self.pitch = pitch
        self.rhythVal = rhythVal

    @classmethod
    def fromPitch(cls, pitch, rhythVal:float) -> Self:
        """
        Constructs a new note given a Pitch object.
        :param pitch: Pitch to provide this note with.
        :param rhythVal: The number of beats this note should
        be played for as a float.
        :return: Note with the given pitch and rhythmic value.
        """
        return cls(pitch,rhythVal)

    @classmethod
    def fromName(cls, noteName:str, octave:int, rhythVal:float) -> Self:
        """
        Constructs a new note given a note name and octave.
        :param noteName: Note name to give to the pitch of this note
        Ex. "A", "Bb", "C#"
        :param octave: Integer between the lower and upper octave
        limits specified in ValConstants.
        :param rhythVal: The number of beats this note should
        be played for as a float.
        :return: Note with the given pitch and rhythmic value.
        """
        pitch = Pitch(noteName,octave)
        return cls(pitch,rhythVal)

    def __str__(self):
        """
        :return: A string representing this note.
        Ex. "A5 1.0", "Bb7 0.5"
        """
        return self.getName() + str(self.getOctave()) + " " + str(self.getRhythVal())

    def interval(self,other):
        """
        Gets the interval between this note and the given note
        in semitones as an integer.
        :param other: Approach note.
        :return: An integer >0 if this note is below the given note,
        <0 if it is above the given note, and 0 if they share the same
        pitch.
        """
        if not isinstance(other, Note):
            raise TypeError("Please input a Note object.")
        else:
            return vu.interval(self,other)

    def getPitch(self):
        """
        :return: The Pitch object that is represented by this note.
        """
        return self.pitch

    def getName(self):
        """
        :return: Name of this note as a string, listing
        note name and octave.
        Ex. "A5", "F#3", "Gb7"
        """
        return self.pitch.getName()

    def getMIDI(self):
        """
        :return: MIDI number of this note as an int.
        Values between 0 - 127, from C-1 to G9.
        """
        return self.pitch.getMIDI()

    def getFreq(self):
        """
        :return: Frequency of this note as a float.
        """
        return self.pitch.getFreq()

    def getOctave(self):
        """
        :return: Octave of this note as an int.
        """
        return self.pitch.getOctave()

    def getRhythVal(self):
        """
        :return: Rhythmic value of this note as a float.
        """
        return self.rhythVal

    def compareRhythVal(self, other):
        """
        Compare the rhythmic value of this note to the given note.
        :param other: Note to compare this note's rhythmic value with.
        :return: The difference between the given note's rhythmic value and
        this note in beats, as a float. Positive values indicate that this
        note is longer than the given note and vice versa; a return value of
        0 means the two are of the same value.
        """
        if not (isinstance(other,Note)):
            raise TypeError("Please input a Note object.")
        else:
            thisVal = self.getRhythVal()
            otherVal = other.getRhythVal()
            return thisVal - otherVal

    def comparePitch(self, other):
        """
        Compares the pitch of this note to the given note.
        :param other: Note to compare this note's pitch with.
        :return: The difference between the given note's pitch and
        this note in semitones, as an int. Positive values indicate that
        this note is higher in pitch than the given note and vice versa;
        a return value of 0 means the two are the same pitch.
        """
        if not (isinstance(other, Note)):
            raise TypeError("Please input a Note object.")
        else:
            return self.getPitch() == other.getPitch()

    def __eq__(self, other):
        """
        Determines whether this note is equal to the
        given note. Notes are equal if they share the same
        pitch and duration. Notes do not have to share
        note names to have the same pitch; enharmonic
        equivalence is accounted for.
        :param other: Note to check for equality with.
        :return: True if this note is equivalent to the
        given note, and false otherwise.
        """
        if not (isinstance(other,Note)):
            return False
        else:
            samePitch = self.comparePitch(other) == 0
            sameRhythVal = self.compareRhythVal(other) == 0
            return samePitch and sameRhythVal