import unittest
import src.main.Python.Model.Note as Note
import src.main.Python.Model.ValUtil as vu
import src.main.Intents.Intent as Intent

class NoteTestCase(unittest.TestCase):

    def setUp(self):
        self.intent = Intent.Intent()

    def test_GetNotes(self):
        F3 = Note.Note(noteName="F", octave=3)
        G3 = Note.Note(noteName="G", octave=3)
        A3 = Note.Note(noteName="A", octave=3)
        B3 = Note.Note(noteName="B", octave=3)
        C4 = Note.Note(noteName="C", octave=4)
        D4 = Note.Note(noteName="D", octave=4)
        E4 = Note.Note(noteName="E", octave=4)
        F4 = Note.Note(noteName="F", octave=4)
        G4 = Note.Note(noteName="G", octave=4)
        expected = (F3,G3,A3,B3,C4,D4,E4,F4,G4)
        actual = vu.getNotes(self.intent)
        self.assertEqual(expected,actual,
                         "Gets a list of Notes that express this Intent's range.")