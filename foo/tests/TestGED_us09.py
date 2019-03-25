import unittest
import datetime
import sys
import os
from GED import Repository


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
a = Repository(filename='Project01_Xiaomeng Xu.ged', dir_path=os.path.join(docs_dir, 'docs'))

class TestUS09(unittest.TestCase):
    def test_us09_birth_b4_parents_death(self):
        self.assertTrue(a.us09_birth_b4_parents_death('@I1@'))
        self.assertTrue(a.us09_birth_b4_parents_death('@I5@'))
        self.assertTrue(a.us09_birth_b4_parents_death('@I6@'))
        self.assertTrue(a.us09_birth_b4_parents_death('@I7@'))
        with self.assertRaises(ValueError):
            a.us09_birth_b4_parents_death('@I2@')
            a.us09_birth_b4_parents_death('@I3@')
            a.us09_birth_b4_parents_death('@I10@')
            a.us09_birth_b4_parents_death('@I4@')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit = False, verbosity= 2)
