import unittest
import src.main.Python.Model.Note as Note

class NoteTestCase(unittest.TestCase):

    def test_EnharmonicBasics(self):
        """Various test of determining enharmonic equivalence."""
        C4 = Note.Note("C", octave=4)
        Bs3 = Note.Note("B#", octave=3)
        Ab3 = Note.Note("Ab", octave=3)
        Gs3 = Note.Note("G#", octave=3)

        self.assertTrue(C4.overlap(C4),
                        "A note is enharmonically equivalent to itself.")
        self.assertTrue(C4.overlap(Bs3),
                        "C4 is enharmonically equivalent to B#3.")
        self.assertTrue(Bs3.overlap(C4),
                        "Enharmonic equivalence is symmetric--if a = b, then b = a.")
        self.assertTrue(Ab3.overlap(Gs3),
                        "Ab3 is enharmonically equivalent to G#3.")


    def test_EnharmonicsFalse(self):
        """These notes should not be enharmonically equivalent."""
        C4 = Note.Note("C", octave=4)
        A4 = Note.Note("A", octave=4)
        C5 = Note.Note("C", octave=5)

        self.assertFalse(C4.overlap(A4),
                         "Same octave and accidental, different name.")
        self.assertFalse(C4.overlap(C5),
                         "Same name and accidental, different octave.")