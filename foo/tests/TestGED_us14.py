import unittest
import datetime
import sys
import os
from GED import Repository

docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
a = Repository(filename='Project01_Xiaomeng Xu.ged', dir_path=os.path.join(docs_dir, 'docs'))
b = Repository(filename='Project_t14.ged', dir_path=os.path.join(docs_dir, 'docs'))

class test_us_14(unittest.TestCase):
    """Test us14_multiple_birth_less_5"""

    def test_family_a(self):
        """test conduct on file 'Project01_Xiaomeng Xu.ged'"""
        self.assertEqual(a.us14_multiple_birth_less_5(), [])

    def test_family_b(self):
        """test conduct on file 'Project_t14.ged'"""
        self.assertEqual(b.us14_multiple_birth_less_5(), ['Error: FAMILY<@F4@>'])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit = False, verbosity= 2)



