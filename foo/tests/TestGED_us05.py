"""SSW555_HomeWork 4
    Xiaomeng Xu"""

import unittest
from GED import Repository
import os


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
GED1 = Repository(filename='Project01_Xiaomeng Xu.ged', dir_path=os.path.join(docs_dir, 'docs'))
GED2 = Repository(filename='Project02.ged', dir_path=os.path.join(docs_dir, 'docs'))
class Test_us05_marriage_b4_death(unittest.TestCase):
    """This are the test cases for user story_05: check if a individual's marriage date is before death date."""
    
    def test_GED1(self):
        """Testing function on file: Project01_Xiaomeng Xu.ged"""
        self.assertEqual(GED1.us05_marriage_b4_death(), [])
    
    
    def test_GED2(self):
        """Testing function on file: Project02.ged"""
        self.assertEqual(GED2.us05_marriage_b4_death(), ['ERROR: FAMILY:<@F2@>', 'ERROR: FAMILY:<@F3@>', 'ERROR: FAMILY:<@F3@>'])





if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit = False, verbosity= 2)
