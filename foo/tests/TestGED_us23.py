import unittest
import datetime
import sys
import os
from GED import Repository


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
a = Repository(filename='Project_t24.ged', dir_path=os.path.join(docs_dir, 'docs'))

class Test_us23_a(unittest.TestCase):
    """Tests conducted on file 'Project_t24.ged'"""

    def test_us23_a(self):
        """Test us23_unique_name_and_birthday()"""
        self.assertEqual(a.us23_unique_name_and_birthday(), ['ANOMALY: INDIVIDULE:<@I1@>', 
        'ANOMALY: INDIVIDULE:<@I4@>', 
        'ANOMALY: INDIVIDULE:<@I6@>', 
        'ANOMALY: INDIVIDULE:<@I8@>', 
        'ERROR: INDIVIDULE:<@I9@>', 
        'ERROR: INDIVIDULE:<@I10@>', 
        'ERROR: INDIVIDULE:<@I11@>', 
        'ERROR: INDIVIDULE:<@I12@>', 
        'ERROR: INDIVIDULE:<@I13@>', 
        'ANOMALY: INDIVIDULE:<@I18@>', 
        'ANOMALY: INDIVIDULE:<@I19@>', 
        'ANOMALY: INDIVIDULE:<@I20@>'])

b = Repository(filename='Project01_Xiaomeng Xu.ged', dir_path=os.path.join(docs_dir, 'docs'))

class Test_us23_b(unittest.TestCase):
    """Tests conducted on file 'Project01_Xiaomeng Xu.ged'"""

    def test_us23_b(self):
        """Test us23_unique_name_and_birthday()"""
        self.assertEqual(b.us23_unique_name_and_birthday(), [])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
