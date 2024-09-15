"""
Models a certain pitch. Can be represented as a
note name and octave, a MIDI note number, or a frequency.
Can determine whether it is an enharmonic equivalent to
another pitch.
"""

import src.main.Python.Model.ValUtil as vu

class Pitch:

    def __init__(self, name, octave):
        if not vu.validateNoteName(name):
            raise Exception("Unrecognized note name.")
        else:
            self.noteName = name
            self.octave = octave
            self.MIDI = vu.MIDIFromPitch(self.noteName, self.octave)
            self.freq = self._nameToFreq()

    # TODO: Move to ValUtil and replace with Pitch
    def _nameToFreq(self):
        """
        Returns the frequency associated with this note.
        :return: The frequency of this note if it is within
        the acceptable range of MIDI notes (C-1 - G9) as a double.
        """
        # Edge case for A4
        name = self.getName()
        octave = self.getOctave()
        A4Freq = 440.0
        if (name == "A" and octave == 4):
            return A4Freq
        else:
            A4 = Pitch(name="A", octave=4)
            distanceFromA4 = A4.interval(self)
            freq = A4Freq * pow(2.0, (distanceFromA4 / 12.0))
            return freq

    # Getters
    def getName(self):
        # Change
        """
        :return: Pitch of this note, or note name and octave,
        as a string.
        Ex. "A5", "F#3", "Gb7"
        """
        return self.noteName

    # Add getNote()

    def getMIDI(self):
        """
        :return: MIDI number of this note as an int.
        Values between 0 - 127, from C-1 to G9.
        """
        return self.MIDI

    def getFreq(self):
        """
        :return: Frequency of this note as a float.
        """
        return self.freq

    def getOctave(self):
        # Change
        """
        :return: Octave of this note as an int.
        """
        return self.octave

    # Determining equivalence
    def _distanceFrom(self, other):
        # Move to Pitch
        """
        Determines how many steps are between this note and the given note.
        This does not account for octave or accidental,
        and does not determine whether the notes share a pitch.
        Raises a TypeError if the given note is not of the Note class.
        :param other: Note to check for adjacency with.
        :return: An integer >0 if this note's name is below the given note,
        <0 if it is above the given note, and 0 if the two are of the same name
        without an accidental.
        """
        if not (isinstance(other,Pitch)):
            raise TypeError("Please input a Pitch object.")
        else:
            # Disregard any accidentals for now.
            thisNoAcc = self.getName()[0]
            otherNoAcc = other.getName()[0]

            # Check for the wrap-around from G to A or vice versa.
            exceptions = {"G":"A"}
            keys = exceptions.keys()
            if (thisNoAcc in keys):
                checkOther = exceptions[thisNoAcc]
                if (otherNoAcc == checkOther):
                    return 1
            elif (otherNoAcc in keys):
                checkThis = exceptions[otherNoAcc]
                if (thisNoAcc == checkThis):
                    return -1
            else:
                # Check distance between notes--not semitones, lexicographic!
                return ord(otherNoAcc) - ord(thisNoAcc)

    def _enharmonicExceptions(self, other):
        """
        Helper function that handles edge cases for determining
        whether two notes are enharmonic equivalents.
        :param other: Note to check for enharmonic exception.
        :return: True if the given notes are of an enharmonic pair
        described below, false if not.
        """
        # Maybe add another check here?
        exceptions = {"E#": "F", "B#": "C",
                      "E": "Fb", "B": "Cb"}
        thisName = self.getName()
        otherName = other.getName()
        keys = exceptions.keys()
        if (thisName in keys):
            checkOther = exceptions[thisName]
            if (otherName == checkOther):
                return True
        elif (otherName in keys):
            checkThis = exceptions[otherName]
            if (thisName == checkThis):
                return True
        else:
            return False

    def _enharmonic(self, other):
        """
        Determines whether this note is an enharmonic
        spelling of the given note, i.e. if the two are
        different names for the same pitch. Throws a
        TypeError if the given object is not a Note.
        This does not return true if the two notes have
        the same name.
        Ex. A#._enharmonic(Bb) --> True
            A#._enharmonic(B) --> False
        :param other: Note to check enharmonic equivalence with.
        :return: True if this note is an enharmonic equivalent to
        the given note, and false if otherwise.
        """
        if not (isinstance(other,Pitch)):
            raise TypeError("Please input a Pitch object.")
        else:
            # Check if notes are adjacent to each other.
            stepsTo = self._distanceFrom(other)
            adjacentHigh = stepsTo == -1
            adjacentLow = stepsTo == 1
            adjacent = adjacentHigh or adjacentLow
            sameOct = self._octaveEquivalence(other)
            thisName = self.getName()
            otherName = other.getName()
            if not (sameOct and adjacent):
                return False
            else:
                if(self._enharmonicExceptions(other)):
                    return True
                else:
                    if (adjacentLow):
                        thisSharp = "#" in thisName
                        otherFlat = "b" in otherName
                        return thisSharp and otherFlat
                    else:
                        # Must be adjacentHigh because of earlier check.
                        thisFlat = "b" in thisName
                        otherSharp = "#" in otherName
                        return thisFlat and otherSharp

    def _octaveEquivalence(self, other):
        """
        Determines whether two notes are of the
        same octave, with edge cases for the transition
        between octaves at B# or Cb. Raises a TypeError
        if the given note is not of the Note class.
        :param other: Note to compare octaves with.
        :return: True if both notes share the same octave,
        False if not. If notes are against the change of
        octaves (Ex. B#4 and C5), returns True if they are
        an enharmonic pair.
        """
        if not (isinstance(other,Pitch)):
            raise TypeError("Please input a Pitch object.")
        else:
            thisOct = self.getOctave()
            otherOct = other.getOctave()
            exceptions = {"C":"B#","Cb":"B"}
            thisName = self.getName()
            otherName = other.getName()
            keys = list(exceptions.keys())
            if (thisName in keys) and (exceptions[thisName] == otherName):
                return thisOct - otherOct == 1
            elif (otherName in keys) and (exceptions[otherName] == thisName):
                return otherOct - thisOct == 1
            else:
                return thisOct == otherOct

    def _sameSpelling(self,other):
        """
        Determines whether this note and the given note
        are the same spelling of the same pitch. Note that
        this does not cover enharmonic equivalence.
        Ex. A#4._sameSpelling(A#4) --> True
            A#4._sameSpelling(Bb4) --> False
        :param other: Note to check for exact equivalence with.
        :return: True if this note is spelled the same as
        the given note, and false if not.
        """
        if not (isinstance(other,Pitch)):
            raise TypeError("Please input a Pitch object.")
        else:
            thisName = self.getName()
            thisOct = self.getOctave()
            otherName = other.getName()
            otherOct = other.getOctave()
            return (thisName == otherName) and (thisOct == otherOct)

    def compareTo(self, other):
        if not (isinstance(other, Pitch)):
            raise TypeError("Please input a Pitch object.")
        else:
            if (self == other):
                return 0
            else:
                # Inverting the result of the interval() function, as it
                # treats the second argument as an approach note.
                return -self.interval(other)

    def interval(self,other):
        """
        Gets the interval between this pitch and the given pitch
        in semitones as an integer.
        :param other: Approach note.
        :return: An integer >0 if this note is below the given note,
        <0 if it is above the given note, and 0 if they share the same
        pitch.
        """
        if not isinstance(other, Pitch):
            raise TypeError("Please input a Pitch object.")
        else:
            return vu.interval(self,other)

    def __eq__(self, other):
        """
        Check for equivalence with another Pitch object. Two pitches
        are equivalent if they are spelled the same or if they are
        enharmonic equivalents.
        Ex. A5 == A5 -> True    A#5 == Bb5 -> True    A#5 == Bb4 -> False
        :param other: Pitch object to compare to.
        :return: True if this pitch is equivalent to the given pitch,
        false otherwise.
        """
        if not (isinstance(other, Pitch)):
            return False
        else:
            return self._sameSpelling(other) or self._enharmonic(other)