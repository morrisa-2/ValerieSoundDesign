import unittest
import src.main.Note as Note

class NoteTestCase(unittest.TestCase):

    def test_EnharmonicBasics(self):
        """Various test of determining enharmonic equivalence."""
        C4 = Note.Note("C",octave=4)
        Bs3 = Note.Note("B#",octave=3)
        Db4 = Note.Note("Db",octave=4)

        self.assertTrue(C4.overlap(C4),
                        "A note is enharmonically equivalent to itself.")
        self.assertTrue(C4.overlap(Bs3),
                        "C4 is enharmonically equivalent to B#3.")
        self.assertTrue(C4.overlap(Db4),
                        "C4 is enharmonically equivalent to Db4.")

    def test_EnharmonicsFalse(self):
        """These notes should not be enharmonically equivalent."""
        C4 = Note.Note("C", octave=4)
        A4 = Note.Note("A", octave=4)
        C5 = Note.Note("C", octave=5)

        self.assertFalse(C4.overlap(A4),
                         "Same octave and accidental, different name.")
        self.assertFalse(C4.overlap(C5),
                         "Same name and accidental, different octave.")