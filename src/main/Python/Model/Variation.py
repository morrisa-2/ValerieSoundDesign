"""
Models a single variation produced by the VariationGen class.
"""
import random
import src.main.Python.Model.ValUtil as vu

from src.main.Python.Model.Contour import Contour
from src.main.Python.Model.Note import Note
from src.main.Python.Model.Pitch import Pitch
from src.main.Python.Model.Intent import Intent


class Variation:

    def __init__(self,intent:Intent, prototypical:bool=False):
        """
        Non-default constructor.
        :param intent: Intent to generate variation of.
        Must be an Intent object.
        :param prototypical: Whether this variation is to be
        prototypical or not. The qualities of a prototypical
        variation are outlined in _protoPopulate().
        """
        if not (isinstance(prototypical, (bool,type(None)))):
            raise TypeError("Please input the prototypical parameter as a a boolean.")
        else:
            self.intent = intent

            if prototypical:
                # Rhythm selection MUST occur before population--
                # do not reorder these!!
                self.rhythm = self.intent.getRhythm()
                self.notes = self._protoPopulate()
            else:
                # Same as above!!
                self.rhythm = self._pickRhythm()
                self.notes = self._populate()

    def __str__(self):
        """
        Returns a string representation of this
        variation.
        :return: A string representing this variation.
        Ex. "Notes: A5 B5
             Rhythm: 2 1"
             Intent: Hello
        """
        toJoin = []
        for note in self.notes:
            noteStr = str(note)
            toJoin.append(noteStr)
        return ("Notes: " + str.join(" ",toJoin) +
                "\nRhythm: " + str(self.getRhythm()) +
                "\nIntent: " + str(self.getIntent()))

    def getIntent(self):
        """
        :return: This Variation's Intent.
        """
        return self.intent

    def getTempo(self):
        """
        :return: This Variation's tempo as an int.
        """
        return self.getIntent().getTempo()

    def _inRange(self, pitch):
        """
        Determines whether the given pitch is in the range
        of this variation.
        :param pitch: Pitch to check.
        :return: True if the given note is within range,
        false otherwise.
        """
        if not (isinstance(pitch, Pitch)):
            raise TypeError("Please input a Pitch object.")
        else:
            intent = self.getIntent()
            centralNote = intent.getCentralPitch()

            interval = pitch.interval(centralNote)
            pitchRange = intent.getPitchRange()
            return abs(interval) <= pitchRange

    def lengthInSeconds(self):
        """
        Gets the length of this variation in seconds.
        :return: The length of this variation in seconds as an integer.
        """
        rhythm = self.getRhythm()
        totalBeats = sum(rhythm.getDurations())
        tempo = self.intent.getTempo()
        beatsPerSecond = tempo / 60
        return totalBeats / beatsPerSecond

    def nameOfIntent(self):
        """
        Gets the name of this variation's intent.
        :return: This variation's intent as a string.
        """
        return str(self.intent)

    def _populate(self):
        """
        Populates this variation with notes.
        :return: A tuple of notes to be played
        and recorded for this variation.
        """
        availablePitches = self._findAvailablePitches()
        pitches = self._start(availablePitches)
        length = len(self.rhythm)
        for i in range(1,length):
            pitches = self._conditionalSelection(availablePitches, pitches)
        notes = self._applyDurations(pitches)
        return tuple(notes)

    def _protoPopulate(self):
        """
        Populates this variation with notes that satisfy all
        the conditions outlined below.
        To be considered prototypical, a variation must:
        - Contain its Intent's central note and interval
        - Follow its Intent's designated rhythm
        :return: A tuple of notes to be played and
        recorded for this variation.
        """
        availablePitches = self._findAvailablePitches()
        pitches = self._startOrForce(availablePitches)
        rhythmLength = len(self.getRhythm())

        # _protoConditional will always add two notes to pitches on the final
        # pass, so only run it as many times as
        while rhythmLength - len(pitches) >= 2:
            pitches = self._protoConditional(availablePitches, pitches)

        notes = self._applyDurations(pitches)
        return tuple(notes)



    def getMIDINotes(self):
        toReturn = []
        for note in self.notes:
            toReturn.append(note.getMIDI())
        return tuple(toReturn)

    def getFrequencies(self):
        toReturn = []
        for note in self.notes:
            toReturn.append(note.getFreq())
        return tuple(toReturn)

    def getRhythm(self):
        return self.rhythm.getDurations()

    def _applyDurations(self, applyTo):
        """
        Given a list of pitches, applies the rhythm of this variation
        to create a list of this Variation's notes.
        :param applyTo: List of pitches to apply rhythms to.
        :return: A list of Note objects with the desired
        pitches and rhythmic values.
        """
        self._validateListOfNotes(applyTo)

        length = len(self.rhythm)
        toReturn = []

        for i in range(0,length):
            pitch = applyTo[i]
            duration = self.rhythm.getAt(i)
            name = pitch.getName()
            octave = pitch.getOctave()
            note = Note.fromName(noteName=name, octave=octave, rhythVal=duration)
            toReturn.append(note)

        return toReturn

    def _pickRhythm(self):
        """
        Chooses the rhythm to use for this variation.
        :return: This variation's rhythm.
        """
        intent = self.getIntent()
        sides = 3
        die = random.randrange(0,sides)
        if die == 0:
            return intent.getRhythm()
        else:
            return vu.pullRhythmFromPool()

    def _intervals(self, checkIntOf):
        """
        Given a list of at least two pitches, returns
        a list containing the difference in semitones
        between those pitches in order. If checkIntOf
        has one note, returns an empty list. If checkIntOf
        is empty or contains objects that are not of the Pitch class,
        raises an exception.
        Ex. checkIntOf = [C4,G4,D4];
        returns [7,-5]
        :param checkIntOf: A list of Pitches to check the
        intervals between.
        :return: A list of the intervals between Pitches in
        checkIntOf; an empty list if checkIntOf has one Pitch.
        """
        toReturn = []
        i = 0
        if(len(checkIntOf) < 1):
            raise Exception("checkIntOf must contain at least one note.")
        else:
            self._validateListOfNotes(checkIntOf)
            for note in checkIntOf[:-1]:
                next = checkIntOf[i+1]
                toReturn.append(vu.interval(note,next))
            return toReturn

    def _validateListOfPitches(self,toVal):
        """
        Helper function that raises an error if the given list contains
        any values that are not of the Pitch class.
        :param toVal: List of objects to validate.
        """
        if not all(isinstance(pitch, Pitch) for pitch in toVal):
            raise TypeError("All elements in the given list must be of the Pitch class.")

    def _validateListOfNotes(self,toVal):
        """
        Helper function that raises an error if the given list contains
        any values that are not of the Note class.
        :param toVal: List of objects to validate.
        """
        if not all(isinstance(note, Note) for note in toVal):
            raise TypeError("All elements in the given list must be of the Note class.")

    # Passing toAdd into and out of these selection functions
    # feels weird, though I can't place why.
    # TODO: Consider alternatives to toAdd
    def _selectOnContour(self, availablePitches, addTo):
        """
        Select the next pitch in this sequence based on
        the contour of this intent.
        :param availablePitches: Pitches to select from.
        :param addTo: List to add the next pitch to.
        :return: toAdd with an additional note appended.
        """
        self._validateListOfNotes(addTo)
        self._validateListOfNotes(availablePitches)

        intent = self.getIntent()
        contour = intent.getContour()
        turnAroundRange = 3
        current = addTo[-1]

        # Setting ranges at which an ascending contour will stop looking for
        # higher notes, and vice versa for descending.
        topOut = current not in availablePitches[-turnAroundRange:]
        bottomOut = current not in availablePitches[:turnAroundRange]
        currentIndex = availablePitches.index(current)

        # If contour is ascending and we're not in the warning range,
        # pick a note at random above the current note.
        if(contour == Contour.ASCENDING and not topOut):
            higherThanCurrent = random.choice(availablePitches[currentIndex:])
            addTo.append(higherThanCurrent)

        # Vice versa for descending
        elif(contour == Contour.DESCENDING and not bottomOut):
            lowerThanCurrent = random.choice(availablePitches[:currentIndex])
            addTo.append(lowerThanCurrent)

        # Pick a random note that isn't the current note.
        else:
            anyButCurrent = random.choice(availablePitches)
            while(anyButCurrent == current):
                anyButCurrent = random.choice(availablePitches)
            addTo.append(anyButCurrent)
        return addTo

    def _selectOnInterval(self, availablePitches, addTo):
        """
        Select the next Pitch in this sequence based on
        the interval of this intent. Selects direction of
        interval based on whether there is room in the range
        of available Pitches, not contour. If there is no room
        on either side, raises an index exception. If neither
        pitch is in key, returns addTo as it was passed in originally.
        :param availablePitches: Pitch to select from.
        :param addTo: List to add the next Pitch to.
        :return: addTo with an additional note appended.
        """
        self._validateListOfPitches(addTo)
        self._validateListOfPitches(availablePitches)

        current = addTo[-1]
        desiredInterval = self.getIntent().getInterval()
        pickBetween = []
        for pitch in availablePitches:
            interval = pitch.interval(current)
            if (abs(interval) == desiredInterval):
                pickBetween.append(pitch)

        if (len(pickBetween) > 0):
            addTo.append(random.choice(pickBetween))

        return addTo

    def _conditionalSelection(self, availablePitches, addTo):
        """
        Selection method based on the Pitches remaining in
        this variation. If the central Pitch has not yet
        been selected for this variation, the chance it
        is selected next is 1/x where x is the remaining
        number of pitches in the pattern. The same is true of
        the intent's interval. If neither has been selected by
        the final Pitch and the central Pitch cannot be reached by
        that interval, one supersedes the other based on the
        _chooseToSupersede() function. If both conditions are met,
        selects a new Pitch based on contour. Raises an exception
        if attempting to add beyond the length of the intent.

        :param availablePitches: Pitches to select from.
        :param addTo: List to add Pitches to.
        :return: addTo with the selected note added.
        """
        self._validateListOfPitches(addTo)
        self._validateListOfPitches(availablePitches)

        intent = self.getIntent()
        intervals = self._intervals(addTo)
        intervalMissing = intent.getInterval() not in intervals
        centralMissing = intent.getCentralNote() not in addTo

        pitchesRemaining = len(self.rhythm) - len(addTo)

        if (pitchesRemaining <= 0):
            raise Exception("Cannot add notes beyond the length of this intent.")
        else:
            if (pitchesRemaining == 1 and centralMissing and intervalMissing):
                return self._chooseToSupersede(availablePitches, addTo)
            else:
                # Pick a random number between 0 and the number of pitches remaining.
                randomByLength = random.randrange(pitchesRemaining)

                if (randomByLength == 0 and intervalMissing):
                    selectOnInt = self._selectOnInterval(availablePitches, addTo)

                    # If the above worked, there will be another note in selectOnInt--
                    # check its length against addTo.
                    if len(selectOnInt) > len(addTo):
                        return selectOnInt
                    else:
                        # Neither of the notes we could get from moving by this interval
                        # are in range/key--just add by contour.
                        return self._selectOnContour(availablePitches, addTo)

                elif (randomByLength == 0 and centralMissing):
                    return self._addCentral(addTo)
                else:
                    return self._selectOnContour(availablePitches, addTo)

    def _protoConditional(self, availablePitches, addTo):
        """
        Use to select notes for a prototypical variation that is more than two notes
        in length. Selects notes based on contour until the final two notes are
        reached, then fills the last two notes via _forceIntAndCenter().
        :param availablePitches: List of pitches to select from.
        :param addTo: List of pitches to add to.
        :return: addTo with the selected pitch or pitches added.
        """
        rhythmLength = len(self.getRhythm())
        addToLength = len(addTo)

        twoRemaining = rhythmLength - addToLength == 2
        lessThanTwoRemaining = rhythmLength - addToLength < 2

        if lessThanTwoRemaining:
            raise Exception("addTo must have two remaining slots for pitches.")

        if twoRemaining:
            return self._forceIntAndCenter(availablePitches,addTo)
        else:
            return self._selectOnContour(availablePitches,addTo)

    def _chooseToSupersede(self, availableNotes, addTo):
        """
        Helper function for conditional selection. Randomly
        chooses between selecting by interval or selecting
        the central Pitch.
        :param availableNotes: List of available notes,
        as any container with the __getitem__() method.
        :param addTo: List of Pitches to add selection to.
        :return: addTo with the selected Pitch appended.
        """
        coinFlip = random.randrange(2)
        if (coinFlip == 0):
            selectOnInt = self._selectOnInterval(availableNotes, addTo)

            # If the above worked, there will be another note in selectOnInt--
            # check its length against addTo.
            if len(selectOnInt) > len(addTo):
                return selectOnInt
            else:
                return self._addCentral(addTo)
        else:
            return self._addCentral(addTo)

    def _startOrForce(self, availablePitches):
        """
        For use with prototypical variations only. Chooses
        whether to immediately force this variation to satisfy
        the central note and interval conditions, or to start
        as normal.
        :param availablePitches:
        :return:
        """
        rhythmLength = len(self.getRhythm())
        if rhythmLength <= 2:
            return self._forceIntAndCenter(availablePitches, [])
        else:
            return self._start(availablePitches)

    def _forceIntAndCenter(self, availablePitches, addTo):
        """
        Given a list of notes that has at least two available
        slots remaining (len(rhythm) - len(addTo) >= 2), adds
        the most desirable combination of two notes that fulfills
        both the central note and interval requirements.
        Desirability is based on the contour of the intent,
        the current note, and whether either condition has
        already been met.
        :param availablePitches: List of available notes, as any
        container with the __getitem__() method.
        :param addTo: List of notes to add to.
        :return: addTo with the two selected pitches added.
        """
        rhythmLen = len(self.getRhythm())
        atLeast2Spots = rhythmLen - len(addTo) >= 2
        if not atLeast2Spots:
            raise Exception("addTo must have at least two remaining spots.")
        else:
            toAdd = self._intOrCenter(availablePitches)
            addTo.append(toAdd)
            centralNote = self.intent.getCentralPitch()
            if toAdd is not centralNote:
                return self._addCentral(addTo)
            else:
                return self._selectOnInterval(availablePitches, addTo)
            
    def _intOrCenter(self, availableNotes):
        """
        Chooses either a note that is the designated
        interval's distance from the central note, or
        the central note itself.
        :param availableNotes: Notes to select from.
        :return: Selected note.
        """
        coinFlip = random.randrange(0,2)
        if coinFlip == 0:
            return self._approachCenter(availableNotes)
        else:
            centralNote = self.intent.getCentralPitch()
            return centralNote

    def _approachCenter(self, availableNotes):
        """
        Chooses to either select the note above or
        below the central note by a leap of the desired
        interval.
        :param availableNotes: Notes to select from.
        :return: Selected note.
        """
        coinFlip  = random.randrange(0,2)
        centralIndex = availableNotes.index(self.intent.getCentralPitch())
        interval = self.intent.getInterval()
        if coinFlip == 0:
            return availableNotes[centralIndex + interval]
        else:
            return availableNotes[centralIndex - interval]

    def _addCentral(self,addTo):
        """
        Adds the central Pitch of this intent to the given list.
        :param addTo: List of Pitches to add the central Pitch to.
        :return: addTo with the central Pitch of this intent added.
        """
        central = self.getIntent().getCentralPitch()
        addTo.append(central)
        return addTo

    def _start(self, availablePitches):
        """
        Selects the first Pitch of this variation. Selection
        is restrained to half of available Pitches based on contour.
        If the intent has a descending contour, only select the
        central Pitch or above, and vice versa.
        :param availablePitches: List of Pitches this variation can
        select from, as any container with the __getitem__() function.
        :return: A list containing the first Pitch of this variation.
        """
        self._validateListOfPitches(availablePitches)
        toReturn = []
        contour = self.intent.getContour()

        if (contour == Contour.DESCENDING):
            upperHalf = availablePitches[len(availablePitches) / 2:]
            randNote = random.choice(upperHalf)
            toReturn.append(randNote)
        elif (contour == Contour.ASCENDING):
            lowerHalf = availablePitches[:len(availablePitches) / 2]
            randNote = random.choice(lowerHalf)
            toReturn.append(randNote)
        else:
            toReturn.append(random.choice(availablePitches))
        return toReturn

    def _findAvailablePitches(self):
        return vu.getPitches(self.getIntent())
