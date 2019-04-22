import unittest
import datetime
import sys
import os
from GED import Repository


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
a = Repository(filename='Project_t16.ged', dir_path=os.path.join(docs_dir, 'docs'))

class Test_us16_a(unittest.TestCase):
    """Tests conducted on file 'Project_t16.ged'"""

    def test_family_a(self):
        """Test conducted on file'Project_t16.ged'"""
        self.assertEqual(a.us16_male_last_names(), ['Error: FAMILY:<@F2@>', 'Error: FAMILY:<@F3@>', 'Error: FAMILY:<@F4@>'])

b = Repository(filename='Project01_Xiaomeng Xu.ged', dir_path=os.path.join(docs_dir, 'docs'))

class Test_us16_b(unittest.TestCase):
    """Tests conducted on file 'Project01_Xiaomeng Xu.ged'"""

    def test_family_b(self):
        """Tests conducted on file 'Project01_Xiaomeng Xu.ged'"""
        self.assertEqual(b.us16_male_last_names(), [])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit = False, verbosity= 2)
