"""Unitest for user story 02"""
import unittest
from GED import Repository
import os


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
GED1 = Repository(filename='Project01_Xiaomeng Xu.ged', dir_path=os.path.join(docs_dir, 'docs'))
GED2 = Repository(filename='TestGED_us02.ged', dir_path=os.path.join(docs_dir, 'docs'))
class Test_us02_birth_b4_marriage(unittest.TestCase):
    """This are the test cases for user story_02: check if a individual's birthday is before marriage date."""
    
    def test_GED1(self):
        """Testing function on file: Project01_Xiaomeng Xu.ged"""
        self.assertEqual(GED1.us02_birth_b4_marriage(), [])    
    
    def test_GED2(self):
        """Testing function on file: TestGED_us02.ged"""
        self.assertEqual(GED2.us02_birth_b4_marriage(), ['ANOMALY: FAMILY:<@F2@>', 'ANOMALY: FAMILY:<@F3@>', 'ANOMALY: FAMILY:<@F4@>'])




if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit = False, verbosity= 2)
