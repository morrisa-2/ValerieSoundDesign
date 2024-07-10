import unittest
import test_AvailableNotes as t_AN

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

def load_tests(loader, standard_tests, pattern):
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(t_AN.AvailableNotesTestCase))
    # Rest of cases go here!!
    return suite

if __name__ == '__main__':
    unittest.main()
