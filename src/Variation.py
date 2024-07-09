"""
Models a single variation produced by the VariationGen class.

Invariant:
 -  The Variation refers to a String which is formatted based on Gensound's
    melodic shorthand notation.
 -  A Variation also has reference to the Intent from which it was generated,
    but not the VariationGen that produced it.
"""
import Intents.Intent
import ValConstants as v

class Variation:
    def __init__(self,intent,contents):
        if (intent is type(Intents.Intent)):
            self.intent = intent
        else:
            self.intent = Intents.Intent
        self.contents = contents

    def getIntent(self):
        return self.intent

    def populate(self):
        '''
             1.    Find intent central note in the notes list
             2.    Combine key, mode, and pitch range to select which
                  notes are available to this variation.
                      2a. Add all notes within the given pitch range
                          to a list.
                      2b. Find the first instance of the key center
                           in the list.
                       2c. Add key center to separate list.
                       2d. Increment based on modal steps, adding each
                           selection to the new list until the end is
                           exceeded.
                       2e. Repeat 2d backwards, starting from the end
                           of the modal list.
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
