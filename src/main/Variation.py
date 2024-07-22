"""
Models a single variation produced by the VariationGen class.

Invariant:
 -  The Variation refers to a String which is formatted based on Gensound's
    melodic shorthand notation.
 -  A Variation also has reference to the Intent from which it was generated,
    but not the VariationGen that produced it.
"""
import random
import src.main.ValConstants as v
import src.main.ValUtil as vu

class Variation:

    def __init__(self,intent):
        """
        Non-default constructor.
        :param intent: Intent to generate variation of.
        Must be an Intent object or a child of Intent.
        """
        # TODO: Check whether given intent is valid
        self.intent = intent
        self.notes = self.populate()

    def prepForSignal(self):
        """
        :return: A tuple of two elements--the notes of this
        variation and its tempo.
        """
        tempo = self.intent.getTempo()
        return (self.notes,tempo)

    def inRange(self,pitch):
        centralIndex = v.NOTES.index(self.intent.getCentralNote())
        pitchRange = self.intent.getPitchRange()
        rangeMin = centralIndex - pitchRange
        rangeMax = centralIndex + pitchRange
        if(pitch in v.NOTES):
            pitchIndex = v.NOTES.index(pitch)
            return pitchIndex <= rangeMax and pitchIndex >= rangeMin
        else:
            raise ValueError('Unrecognized note name.')

    def __str__(self):
        """
        Returns a string representation of this
        variation.
        :return: A string representing this variation.
        Ex. "C5=0.5 G4=2 A3=1 (Intent)"
        """
        return str(self.notes + " ("+str(self.intent)+")")

    def populate(self):
        availableNotes = self.findAvailableNotes()
        toPlay = self.start(availableNotes)
        length = self.intent.getLength()
        for i in range(length - 1):
            toPlay = self.conditionalSelection(availableNotes,toPlay)
        self.applyDurations(toPlay)
        return " ".join(toPlay)

    # This is a provisional solution and is going to sound clunky.
    # TODO: Make rhythms more dynamic--weighting system?
    def applyDurations(self,applyTo):
        """
        Given a list of notes, applies this intent's rhythm--or
        note duration--to the list. If the length of the intent
        exceeds the size of the rhythm, wraps around
        :param applyTo: List of notes to apply rhythms to.
        :return: applyTo with each note modified to reflect
        its duration.
        """
        rhythm = self.intent.getRhythm()
        length = self.intent.getLength()
        i = 0
        toReturn = []
        for note in applyTo:
            if (i >= len(rhythm)):
                i = 0
            toReturn.append(note + "=" + rhythm[i])
            i+=1
        return toReturn

    def intervals(self,checkIntOf):
        """
        Given a list of at least two notes, returns
        a list containing the difference in semitones
        between those notes in order. If checkIntOf
        has one note, returns an empty list. If checkIntOf
        is empty, raises an exception.
        Ex. checkIntOf = ["C4","G4","D4"];
        returns [7,-5]
        :param checkIntOf: A list of notes to check the
        intervals between.
        :return: A list of the intervals between note in
        checkIntOf; an empty list if checkIntOf has one note.
        """
        toReturn = []
        i = 0
        if(len(checkIntOf) < 1):
            raise Exception("checkIntOf must contain at least one note.")
        else:
            for note in checkIntOf[:-1]:
                next = checkIntOf[i+1]
                toReturn.append(vu.interval(note,next))
            return toReturn

    # Passing toAdd into and out of these selection functions
    # feels weird, though I can't place why.
    # TODO: Consider alternatives to toAdd
    def selectOnContour(self,availableNotes,toAdd):
        """
        Select the next note in this sequence based on
        the contour of this intent.
        :param availableNotes: Notes to select from.
        :param toAdd: List to add the next note to.
        :return: toAdd with an additional note appended.
        """
        contour = self.intent.getContour()
        turnAroundRange = 3
        current = toAdd[-1]
        topOut = current not in availableNotes[-turnAroundRange:]
        bottomOut = current not in availableNotes[:turnAroundRange]
        currentIndex = availableNotes.index(current)
        if(contour == v.ASCENDING and not topOut):
            higherThanCurrent = random.choice(availableNotes[currentIndex:])
            toAdd.append(higherThanCurrent)
        elif(contour == v.DESCENDING and not bottomOut):
            lowerThanCurrent = random.choice(availableNotes[:currentIndex])
            toAdd.append(lowerThanCurrent)
        else:
            anyButCurrent = random.choice(availableNotes)
            while(anyButCurrent == current):
                anyButCurrent = random.choice(availableNotes)
            toAdd.append(anyButCurrent)
        return toAdd

    def selectOnInterval(self,availableNotes,fullRange,addTo):
        """
        Select the next note in this sequence based on
        the interval of this intent. Selects direction of
        interval based on whether there is room in the range
        of available notes, not contour. If there is no room
        on either side, raises an index exception. If neither
        note is in key, returns addTo as it was passed in originally.
        :param availableNotes: Notes to select from.
        :param fullRange: Full range of notes surrounding
        the central note, including those outside the desired key.
        :param addTo: List to add the next note to.
        :return: addTo with an additional note appended.
        """
        current = addTo[-1]
        interval = self.intent.getInterval()
        currentIndex = fullRange.index(current)
        roomToGoDown = currentIndex - interval >= 0
        roomToGoUp = currentIndex + interval < len(fullRange)
        if (not roomToGoUp and not roomToGoDown):
            raise IndexError("Desired interval exceeds range.")
        else:
            if (roomToGoDown):
                downInKey = fullRange[currentIndex - interval] in availableNotes
                canGoDown = roomToGoDown and downInKey
            else:
                downInKey = False
                canGoDown = False

            if (roomToGoUp):
                upInKey = fullRange[currentIndex + interval] in availableNotes
                canGoUp = roomToGoUp and upInKey
            else:
                upInKey = False
                canGoUp = False

            if(not upInKey and not downInKey):
                return addTo
            else:
                if(not canGoUp and canGoDown):
                    noteToAdd = fullRange[currentIndex - interval]
                elif(canGoUp and not canGoDown):
                    noteToAdd = fullRange[currentIndex + interval]
                else:
                    coinFlip = random.randrange(2)
                    if (coinFlip == 0):
                        noteToAdd = fullRange[currentIndex - interval]
                    else:
                        noteToAdd = fullRange[currentIndex + interval]

                addTo.append(noteToAdd)
                return addTo

    def conditionalSelection(self,availableNotes,addTo):
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
        intervals = self.intervals(addTo)
        intervalMissing = self.intent.getInterval() not in intervals
        centralMissing = self.intent.getCentralNote() not in addTo
        notesRemaining = self.intent.getLength() - len(addTo)
        if (notesRemaining <= 0):
            raise Exception("Cannot add notes beyond the length of this intent.")
        else:
            if (notesRemaining == 1 and centralMissing and intervalMissing):
                return self.chooseToSupersede(availableNotes,addTo)
            else:
                randomByLength = random.randrange(notesRemaining)
                if (randomByLength == 0 and intervalMissing):
                    return self.selectOnInterval(availableNotes,self.findFullRange(),addTo)
                elif (randomByLength == 0 and centralMissing):
                    addTo.append(self.intent.getCentralNote())
                    return addTo
                else:
                    return self.selectOnContour(availableNotes,addTo)

    def chooseToSupersede(self,availableNotes,addTo):
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
            return self.selectOnInterval(availableNotes, self.findFullRange(), addTo)
        else:
            central = self.intent.getCentralNote()
            addTo.append(central)
            return addTo

    def start(self,availableNotes):
        """
        Selects the first note of this variation. Selection
        is restrained to half of available notes based on contour.
        If the intent has a descending contour, only select the
        central note or above, and vice versa.
        :param availableNotes: List of notes this variation can select from.
        :return: A list containing the first note of this variation.
        """
        toReturn = []
        contour = self.intent.getContour()
        if (contour == v.DESCENDING):
            upperHalf = availableNotes[len(availableNotes)/2:]
            randNote = random.choice(upperHalf)
            toReturn.append(randNote)
        elif (contour == v.ASCENDING):
            lowerHalf = availableNotes[:len(availableNotes) / 2]
            randNote = random.choice(lowerHalf)
            toReturn.append(randNote)
        else:
            toReturn.append(random.choice(availableNotes))
        return toReturn


    def findAvailableNotes(self):
        fullRange = self.findFullRange()
        return self.listOfAvailable(fullRange)

    def findKeyCenter(self,fullRange):
        key = self.intent.getKey()
        notFound = True
        i = 0
        centralIndex = 0
        while (notFound & i < len(fullRange)):
            note = fullRange[i]
            if key in note:
                # Found a matching note name to the key center--check if pitch matches.
                matchPitch = ('#' in key and '#' in note) or ('#' not in key and '#' not in note)
                if matchPitch:
                    notFound = False
                    return i
            else:
                i += 1
        if (notFound):
            raise IndexError('Key center not present in the given range.')

    def listOfAvailable(self,fullRange):
        centralIndex = self.findKeyCenter(fullRange)
        mode = self.intent.getMode()
        pitchRange = self.intent.getPitchRange()
        availableNotes = []
        i = centralIndex
        j = 0
        while (i < len(fullRange)):
            availableNotes.append(fullRange[i])
            i += mode[j]
            j += 1
        j = -1
        i = centralIndex
        while (i > 0):
            i -= mode[j]
            availableNotes.insert(0,fullRange[i])
            j -= 1
        return availableNotes

    def findFullRange(self):
        centralIndex = v.NOTES.index(self.intent.getCentralNote())
        pitchRange = self.intent.getPitchRange()
        if (centralIndex - pitchRange > 0 & centralIndex + pitchRange < len(v.NOTES)):
            fullRange = [pitch for pitch in v.NOTES if self.inRange(pitch)]
            return fullRange
        else:
            raise ValueError('Given range exceeds available pitches.')