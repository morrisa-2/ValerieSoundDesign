import unittest
import src.main.Python.Model.Variation as var
import src.main.Intents.Intent as intent

class ApplyDurationTestCase(unittest.TestCase):

    def setUp(self):
        self.i = intent.Intent()
        self.v = var.Variation(self.i)
        self.availableNotes = self.v.findAvailableNotes()
        self.toPlay = self.v.start(self.availableNotes)

    def tearDown(self):
        self.i = None
        self.v = None
        self.toPlay = None

    # This is going to break when we change the way rhythms are applied.
    # TODO: When rhythm system changes, fix these.
    def test_Duration(self):
        """Applies durations correctly for a variation whose length
        is as long as its rhythm."""
        length = self.i.getLength()
        for i in range(length - 1):
            self.toPlay = self.v.conditionalSelection(self.availableNotes, self.toPlay)
        i = 0
        rhythm = self.i.getRhythm()
        expected = []
        for note in self.toPlay:
            expected.append(note + "=" + rhythm[i])
            i += 1
        actual = self.v.applyDurations(self.toPlay)
        self.assertEqual(expected,actual)

    def test_FallShort(self):
        """Applies durations correctly for a variation whose length
        is shorter than its rhythm."""
        self.i.setLength(2)
        length = self.i.getLength()
        for i in range(length - 1):
            self.toPlay = self.v.conditionalSelection(self.availableNotes, self.toPlay)
        i = 0
        rhythm = self.i.getRhythm()
        expected = []
        for note in self.toPlay:
            expected.append(note + "=" + rhythm[i])
            i += 1
        actual = self.v.applyDurations(self.toPlay)
        self.assertEqual(expected, actual)

    def test_WrapAround(self):
        """Applies durations correctly for a variation whose length
        is longer than its rhythm."""
        self.i.setLength(4)
        length = self.i.getLength()
        for i in range(length - 1):
            self.toPlay = self.v.conditionalSelection(self.availableNotes, self.toPlay)
        i = 0
        rhythm = self.i.getRhythm()
        expected = []
        for note in self.toPlay:
            if (i >= len(rhythm)):
                i = 0
            expected.append(note + "=" + rhythm[i])
            i += 1
        actual = self.v.applyDurations(self.toPlay)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
