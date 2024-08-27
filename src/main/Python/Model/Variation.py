"""
Models a single variation produced by the VariationGen class.

Invariant:
 -  The Variation refers to a String which is formatted based on Gensound's
    melodic shorthand notation.
 -  A Variation also has reference to the Intent from which it was generated,
    but not the VariationGen that produced it.
"""
import random
import src.main.Python.Model.ValConstants as vc
import src.main.Python.Model.ValUtil as vu
from src.main.Python.Model.Note import Note
from src.main.Python.Model.Intent import Intent


class Variation:

    def __init__(self,intent):
        """
        Non-default constructor.
        :param intent: Intent to generate variation of.
        Must be an Intent object or a child of Intent.
        """
        if not (isinstance(intent,Intent)):
            raise TypeError("Intent parameter must be an Intent object.")
        else:
            self.intent = intent
            self.rhythm = self._pickRhythm()
            self.contents = self._populate()

    def getIntent(self):
        """
        :return: This Variation's Intent.
        """
        return self.intent

    def getTempo(self):
        return self.getIntent().getTempo()

    def _inRange(self,note):
        """
        Determines whether the given note is in the range
        of this variation.
        :param note: Note to check.
        :return: True if the given note is within range,
        false otherwise.
        """
        if not (isinstance(note,Note)):
            raise TypeError("Please input an Note object.")
        else:
            intent = self.getIntent()
            centralNote = intent.getCentralNote()
            interval = vu.interval(note,centralNote)
            pitchRange = intent.getPitchRange()
            return abs(interval) <= pitchRange

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
        for note in self.contents:
            noteStr = str(note)
            toJoin.append(noteStr)
        return "Notes: " + str.join(" ",toJoin) + "\n" + "Intent: " + str(self.getIntent())


    def lengthInSeconds(self):
        """
        Gets the length of this variation in seconds.
        :return: The length of this variation in seconds as an integer.
        """
        rhythm = self.getRhythm()
        totalBeats = sum(rhythm)
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
        :return: An array of notes to be played
        and recorded for this variation.
        """
        availableNotes = self._findAvailableNotes()
        notes = self._start(availableNotes)
        length = len(self.rhythm)
        for i in range(1,length):
            notes = self._conditionalSelection(availableNotes, notes)
        notes = self._applyDurations(notes)
        return notes

    def getMIDINotes(self):
        toReturn = []
        for note in self.contents:
            toReturn.append(note.getMIDI())
        return toReturn

    def getFrequencies(self):
        toReturn = []
        for note in self.contents:
            toReturn.append(note.getFreq())
        return toReturn

    def getRhythm(self):
        toReturn = []
        for note in self.contents:
            toReturn.append(note.getRhythVal())
        return toReturn

    # TODO: Switch to Rhythm class.
    def _applyDurations(self, applyTo):
        """
        Given a list of notes, applies the rhythm of this variation
        to those notes.
        :param rhythm: Ordered list of rhythm values to apply.
        :param applyTo: List of notes to apply rhythms to.
        :return: applyTo with each note's rhythmic value adjusted to
        match the rhythm of this variation.
        """
        self._validateListOfNotes(applyTo)

        length = len(self.rhythm)
        toReturn = []

        for i in range(0,length):
            note = applyTo[i]
            duration = self.rhythm.getAt(i)
            name = note.getName()
            octave = note.getOctave()
            copy = Note(noteName=name, octave=octave, rhythVal=duration)
            toReturn.append(copy)

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
        Given a list of at least two notes, returns
        a list containing the difference in semitones
        between those notes in order. If checkIntOf
        has one note, returns an empty list. If checkIntOf
        is empty or contains objects that are not of the Note class,
        raises an exception.
        Ex. checkIntOf = [C4,G4,D4];
        returns [7,-5]
        :param checkIntOf: A list of Notes to check the
        intervals between.
        :return: A list of the intervals between Notes in
        checkIntOf; an empty list if checkIntOf has one note.
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

    def _validateListOfNotes(self,toVal):
        """
        Helper functiont that raises an error if the given list contains
        any values that are not of the note class.
        :param toVal: List of objects to validate.
        """
        if not all(isinstance(notes, Note) for notes in toVal):
            raise TypeError("All elements in the given list must be of the Note class.")

    # Passing toAdd into and out of these selection functions
    # feels weird, though I can't place why.
    # TODO: Consider alternatives to toAdd
    def _selectOnContour(self, availableNotes, addTo):
        """
        Select the next note in this sequence based on
        the contour of this intent.
        :param availableNotes: Notes to select from.
        :param addTo: List to add the next note to.
        :return: toAdd with an additional note appended.
        """
        self._validateListOfNotes(addTo)
        self._validateListOfNotes(availableNotes)
        intent = self.getIntent()
        contour = intent.getContour()
        turnAroundRange = 3
        current = addTo[-1]
        topOut = current not in availableNotes[-turnAroundRange:]
        bottomOut = current not in availableNotes[:turnAroundRange]
        currentIndex = availableNotes.index(current)
        if(contour == vc.ASCENDING and not topOut):
            higherThanCurrent = random.choice(availableNotes[currentIndex:])
            addTo.append(higherThanCurrent)
        elif(contour == vc.DESCENDING and not bottomOut):
            lowerThanCurrent = random.choice(availableNotes[:currentIndex])
            addTo.append(lowerThanCurrent)
        else:
            anyButCurrent = random.choice(availableNotes)
            while(anyButCurrent == current):
                anyButCurrent = random.choice(availableNotes)
            addTo.append(anyButCurrent)
        return addTo

    def _selectOnInterval(self, availableNotes, addTo):
        """
        Select the next note in this sequence based on
        the interval of this intent. Selects direction of
        interval based on whether there is room in the range
        of available notes, not contour. If there is no room
        on either side, raises an index exception. If neither
        note is in key, returns addTo as it was passed in originally.
        :param availableNotes: Notes to select from.
        :param addTo: List to add the next note to.
        :return: addTo with an additional note appended.
        """
        self._validateListOfNotes(addTo)
        self._validateListOfNotes(availableNotes)

        current = addTo[-1]
        desiredInterval = self.getIntent().getInterval()
        pickBetween = []
        for note in availableNotes:
            interval = note.interval(current)
            if (abs(interval) == desiredInterval):
                pickBetween.append(note)

        if (len(pickBetween) > 0):
            addTo.append(random.choice(pickBetween))

        return addTo

    def _conditionalSelection(self, availableNotes, addTo):
        """
        Selection method based on the notes remaining in
        this variation. If the central note has not yet
        been selected for this variation, the chance it
        is selected next is 1/x where x is the remaining
        number of notes in the pattern. The same is true of
        the intent's interval. If neither has been selected by
        the final note and the central note cannot be reached by
        that interval, one supersedes the other at random.
        If both conditions are met, selects a new note based on
        contour. Raises an exception if attempting to add beyond
        the length of the intent.

        :param availableNotes: Notes to select from.
        :param addTo: List to add notes to.
        :return: addTo with the selected note added.
        """
        self._validateListOfNotes(addTo)
        self._validateListOfNotes(availableNotes)
        intent = self.getIntent()
        intervals = self._intervals(addTo)
        intervalMissing = intent.getInterval() not in intervals
        centralMissing = intent.getCentralNote() not in addTo

        # Below is going to break when rhythm system changes
        notesRemaining = len(self.rhythm) - len(addTo)

        if (notesRemaining <= 0):
            raise Exception("Cannot add notes beyond the length of this intent.")
        else:
            if (notesRemaining == 1 and centralMissing and intervalMissing):
                return self._chooseToSupersede(availableNotes, addTo)
            else:
                randomByLength = random.randrange(notesRemaining)
                if (randomByLength == 0 and intervalMissing):
                    return self._selectOnInterval(availableNotes, addTo)
                elif (randomByLength == 0 and centralMissing):
                    addTo.append(self.intent.getCentralNote())
                    return addTo
                else:
                    return self._selectOnContour(availableNotes, addTo)

    def _chooseToSupersede(self, availableNotes, addTo):
        """
        Helper function for conditional selection. Randomly
        chooses between selecting by interval or selecting
        the central note.
        :param availableNotes: List of available notes.
        :param addTo: List of notes to add selection to.
        :return: addTo with the selected note appended.
        """
        coinFlip = random.randrange(2)
        if (coinFlip == 0):
            interval = self._selectOnInterval(availableNotes, addTo)
            if len(interval) > len(addTo):
                return interval
            else:
                return self._addCentral(addTo)
        else:
            return self._addCentral(addTo)

    def _addCentral(self,addTo):
        """
        Adds the central note of this intent to the given list.
        :param addTo: List of notes to add the central note to.
        :return:
        """
        centralName = self.getIntent().getCentralNote()
        centralOct = self.getIntent().getCentralOctave()
        central = Note(noteName=centralName, octave=centralOct)
        addTo.append(central)
        return addTo

    def _start(self, availableNotes):
        """
        Selects the first note of this variation. Selection
        is restrained to half of available notes based on contour.
        If the intent has a descending contour, only select the
        central note or above, and vice versa.
        :param availableNotes: List of notes this variation can select from.
        :return: A list containing the first note of this variation.
        """
        self._validateListOfNotes(availableNotes)
        toReturn = []
        contour = self.intent.getContour()
        if (contour == vc.DESCENDING):
            upperHalf = availableNotes[len(availableNotes)/2:]
            randNote = random.choice(upperHalf)
            toReturn.append(randNote)
        elif (contour == vc.ASCENDING):
            lowerHalf = availableNotes[:len(availableNotes) / 2]
            randNote = random.choice(lowerHalf)
            toReturn.append(randNote)
        else:
            toReturn.append(random.choice(availableNotes))
        return toReturn

    def _findAvailableNotes(self):
        return vu.getNotes(self.getIntent())
