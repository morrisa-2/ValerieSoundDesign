import unittest
import src.main.Python.Model.Variation as var
import src.main.Intents.Intent as intent

class SelectNoteTestCase(unittest.TestCase):

    def setUp(self):
        self.i = intent.Intent()
        self.v = var.Variation(self.i)
        self.availableNotes = self.v.findAvailableNotes()

    def tearDown(self):
        self.i = None
        self.v = None
        self.availableNotes = None
        self.toPlay = None

    # Decided not to implement this yet.
    # def test_CentralLeap(self):
    #     """If the distance between the current note and
    #     the central note is this variation's required interval,
    #     select the central note immediately."""
    #     toPlay = []
    #     centralIndex = self.availableNotes.index(self.i.getCentralNote())
    #     toPlay.append(self.availableNotes[centralIndex - self.i.getInterval()])
    #     self.v.conditionalSelection(self.availableNotes,toPlay)
    #     expected = ["F3","C4"]
    #     self.assertEqual(expected,toPlay)

    def test_CentralNoteProbability(self):
        """If the central note has not been selected,
        the chance of it being selected is 1/x, where
        x = the number of notes still to be selected."""
        toPlay = ["A3","E4"]
        self.v.conditionalSelection(self.availableNotes,toPlay)
        expected = ["A3","E4","C4"]
        self.assertEqual(expected,toPlay)

    def test_CentralIntervalProbability(self):
        """If the required interval has not been selected,
        the chance of it being selected is 1/x, where
        x = the number of notes still to be selected."""
        toPlay = ["A3", "C4"]
        self.v.conditionalSelection(self.availableNotes, toPlay)
        expected1 = ["A3", "C4", "G4"]
        expected2 = ["A3", "C4", "F3"]
        condition = (toPlay == expected1) or (toPlay == expected2)
        self.assertTrue(condition)

    def test_IntervalNoteInterference(self):
        """If there is only one note remaining and
        neither the central note nor interval is present,
        one will supersede the other at random."""
        toPlay = ["A3", "A3"]
        self.v.conditionalSelection(self.availableNotes, toPlay)
        expected1 = ["A3", "A3", "C4"]
        expected2 = ["A3", "A3", "E4"]
        condition = (toPlay == expected1) or (toPlay == expected2)
        self.assertTrue(condition)

if __name__ == '__main__':
    unittest.main()
