import unittest
import datetime
import sys
import os
from GED import Repository


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
a = Repository(filename='Project01_Xiaomeng Xu.ged', dir_path=os.path.join(docs_dir, 'docs'))
b = Repository(filename='Project_t10.ged', dir_path=os.path.join(docs_dir, 'docs'))

class TestUS08(unittest.TestCase):
    def test_us08_birth_b4_parents_marriage(self):
        self.assertTrue(a.us08_birth_b4_parents_marriage('@I1@'))
        self.assertEqual(a.us08_birth_b4_parents_marriage('@I10@'),"Can't find!")
        #with self.assertRaises(ValueError):a.us08_birth_b4_parents_marriage('@I10@')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit = False, verbosity= 2)
