import unittest
import datetime
import sys
import os
from GED import Repository

docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
a = Repository(filename='Project_t14.ged', dir_path=os.path.join(docs_dir, 'docs'))

class test_us_14(unittest.TestCase):
    """Test us14_multiple_birth_less_5
        tests condicted on file 'Project_t14.ged'"""

    def test_family_01(self):
        """test us14_multiple_birth_less_5 on family 1"""
        self.assertEqual(a.us14_multiple_birth_less_5('@F1@'), 'ID: @F1@, Reslut: Good')

    def test_family_02(self):
        """test us14_multiple_birth_less_5 on family 2"""
        self.assertEqual(a.us14_multiple_birth_less_5('@F2@'), 'ID: @F2@, Reslut: Good')

    def test_family_04(self):
        """test us14_multiple_birth_less_5 on family 4"""
        self.assertEqual(a.us14_multiple_birth_less_5('@F4@'), 'ID: @F4@, Reslut: Error: Multiple birth more than 5')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit = False, verbosity= 2)



