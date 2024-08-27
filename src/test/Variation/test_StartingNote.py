import unittest
import src.main.Python.Model.ValConstants as val
import src.main.Python.Model.Variation as var
import src.main.Intents.Intent as intent


class StartingNoteTestCase(unittest.TestCase):
    def setUp(self):
        self.i = intent.Intent()
        self.v = var.Variation(self.i)
        self.availableNotes = self.v.findAvailableNotes()
        self.startNote = (self.v.start(self.availableNotes))[0]

    def tearDown(self):
        self.i = None
        self.v = None

    def test_AscendingStartLowerHalf(self):
        """Ascending contour restrains starting
        selection to the lower half of the range."""
        self.i.setContour(val.ASCENDING)
        startInLowerHalf = self.availableNotes.index(self.startNote) < (len(self.availableNotes)/2)
        self.assertTrue(startInLowerHalf)

    def test_DescendingStartUpperHalf(self):
        """Descending contour restrains starting
        selection to the lower half of the range."""
        self.i.setContour(val.DESCENDING)
        startInUpperHalf = self.availableNotes.index(self.startNote) >= (len(self.availableNotes)/2)
        self.assertTrue(startInUpperHalf)

if __name__ == '__main__':
    unittest.main()
