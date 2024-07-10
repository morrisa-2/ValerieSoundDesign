"""
Models a single variation produced by the VariationGen class.

Invariant:
 -  The Variation refers to a String which is formatted based on Gensound's
    melodic shorthand notation.
 -  A Variation also has reference to the Intent from which it was generated,
    but not the VariationGen that produced it.
"""
import src.main.Intents.Intent
import src.main.ValConstants as v

class Variation:
    def __init__(self,intent):
        """
        Non-default constructor.
        :param intent: Intent to generate variation of.
        Must be an Intent object or a child of Intent.
        """
        # TODO: Check whether given intent is valid
        self.intent = intent
        self.contents = self.populate()

    def inRange(self,pitch):
        centralNote = self.intent.getCentralNote()
        pitchRange = self.intent.getPitchRange()
        rangeMin = centralNote - pitchRange
        rangeMax = centralNote + pitchRange
        if(pitch in v.NOTES):
            pitchIndex = v.NOTES.index(pitch)
            return pitchIndex <= rangeMax and pitchIndex >= rangeMin
        else:
            raise ValueError('Unrecognized note name.')

    # Uncomment when populate is functional.
    # def __str__(self):
    #     """
    #     Returns a string representation of this
    #     variation.
    #     :return: A string representing this variation.
    #     Ex. "C5=0.5 G4=2 A3=1 (Intent)"
    #     """
    #     return str(self.contents + " ("+self.intent+")")

    def populate(self):
        availableNotes = self.findAvailableNotes()
        toPlay = self.start(availableNotes)
        '''   
             3.    Select a starting note.
                       3a. Restrain selection to half of available notes
                           based on contour. If the intent has a descending
                           contour, only select the central note or above,
                           and vice versa.
             4.    Select next note.
                       4a. Check whether the central note has been selected
                           already. If so, ignore 4b and 4c.
                       4b. Check distance between this note and the central
                           note in the list of this variation's full range.
                           If that distance is the interval of this intent,
                           select the central note immediately.
                       4c. Randomly select whether to play the central note
                           or another note in the available range. Proportions
                           are based on the remaining length of the variation. For instance,
                           if a variation has 2 notes remaining and neither 4a nor 4b is
                           satisfied, there is a 50% chance the central note will be
                           selected. If the central note is not selected this time around,
                           the chance it is selected in the next iteration becomes 100%.
                       4d. Select whether the next note will ascend or descend. If the
                           intent has an ascending contour, it is more likely to choose
                           a note above the selection if there is room to do so. The
                           inverse is true of a descending contour.
                       4e. Check whether this intent's interval is already present.
                           If so, ignore 4f.
                       4f. Check whether the desired interval is possible to reach
                           in the given direction. If so, select whether to choose
                           this interval or another to insert. This choice is similarly
                           proportioned to the selection of the central note--see above
                           for details.
                       4g. Insert the note provided by a movement of this interval.
             5.     Repeat step 4 until the variation is of the desired length.
             6.     Add the length of each note to the variation.
                       6a. These are denoted by the rhythmic descriptors in
                           ValConstants--short, mid, and long. Each corresponds to a
                           number (0.5, 1, and 2) which signifies to gensound whether
                           to play an eighth, quarter, or half note.
                       6b. For instance, if the notes in this variation are ["C5","G4","A4"] and
                           the rhythmic pattern is [short,long,mid], the result of this step is
                           the list ["C5=0.5","G4=2","A4=1"].
             7.     Combine the list of notes into a single string and return it.
                       7a. Keeping with the example above, the string should be formatted as
                           such: "C5=0.5 G4=2 A4=1".
            '''
        pass

    def start(self,availableNotes):
        """
        Selects the first note of this variation. Selection
        is restrained to half of available notes based on contour.
        If the intent has a descending contour, only select the
        central note or above, and vice versa.
        :param availableNotes: List of notes this variation can select from.
        :return: A list containing the first note of this variation.
        """
        pass


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
        centralNote = self.intent.getCentralNote()
        pitchRange = self.intent.getPitchRange()
        if (centralNote - pitchRange > 0 & centralNote + pitchRange < len(v.NOTES)):
            fullRange = [pitch for pitch in v.NOTES if self.inRange(pitch)]
            return fullRange
        else:
            raise ValueError('Given range exceeds available pitches.')