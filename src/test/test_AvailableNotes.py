import unittest
import src.main.Variation as var
import src.main.Intents.Intent as intent


class AvailableNotesTestCase(unittest.TestCase):

    def setUp(self):
        self.i = intent.Intent()
        self.v = var.Variation(self.i)

    def tearDown(self):
        self.i = None
        self.v = None

    def test_inRange(self):
        self.assertTrue(self.v.inRange("C4"))
        self.assertTrue(self.v.inRange("G4"))
        self.assertTrue(self.v.inRange("F3"))
        self.assertFalse(self.v.inRange("G#4"))
        self.assertFalse(self.v.inRange("E3"))
        with self.assertRaises(ValueError):
            self.v.inRange("H17")

    def test_findFullRange(self):
        expectedRange = ["F3","F#3","G3","G#3",
                         "A3","A#3","B3","C4",
                         "C#4","D4","D#4","E4",
                         "F4","F#4","G4"]
        self.assertEqual(expectedRange,self.v.findFullRange())

    def test_findKeyCenter(self):
        expected = 7
        fr = self.v.findFullRange()
        self.assertEqual(expected,self.v.findKeyCenter(fr))

    def test_listOfAvailable(self):
        fr = self.v.findFullRange()
        expected = ["F3", "G3", "A3", "B3",
                    "C4", "D4", "E4", "F4", "G4"]
        self.assertEqual(expected,self.v.listOfAvailable(fr))
    def test_findAvailableNotes(self):
        expected = ["F3","G3","A3","B3",
                    "C4","D4","E4","F4","G4"]
        self.assertEqual(expected,self.v.findAvailableNotes())


if __name__ == '__main__':
    unittest.main()
