"""SSW555_HomeWork 4
    Xiaomeng Xu"""

import unittest
from GED import Repository
import os


GED1 = Repository(filename='Project01_Xiaomeng Xu.ged', dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')
GED2 = Repository(filename='Project02.ged', dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')
class Test_us05_marriage_b4_death(unittest.TestCase):
    """This are the test cases for user story_05: check if a individual's marriage date is before death date."""
    
    def test_GED1_family1(self):
        """Testing function on file: Project01_Xiaomeng Xu.ged"""
        self.assertEqual(GED1.us05_marriage_b4_death('@F1@'), 'Family ID: @F1@, Result: No marriage date')
    
    def test_GED1_family2(self):
        """Testing function on file: Project01_Xiaomeng Xu.ged"""
        self.assertEqual(GED1.us05_marriage_b4_death('@F2@'), 'Family ID: @F2@, Result: No marriage date')
    
    def test_GED1_family3(self):
        """Testing function on file: Project01_Xiaomeng Xu.ged"""
        self.assertEqual(GED1.us05_marriage_b4_death('@F3@'), 'Family ID: @F3@, Result: Good')
    
    def test_GED1_family4(self):
        """Testing function on file: Project01_Xiaomeng Xu.ged"""
        self.assertEqual(GED1.us05_marriage_b4_death('@F4@'), 'Family ID: @F4@, Result: Good')
    
    
    def test_GED2_family1(self):
        """Testing function on file: Project02.ged"""
        self.assertEqual(GED2.us05_marriage_b4_death('@F1@'), 'Family ID: @F1@, Result: No marriage date')

    def test_GED2_family2(self):
        """Testing function on file: Project02.ged"""
        self.assertEqual(GED2.us05_marriage_b4_death('@F2@'), 'Family ID: @F2@, Result: Error: Death before marriage')

    def test_GED2_family3(self):
        """Testing function on file: Project02.ged"""
        self.assertEqual(GED2.us05_marriage_b4_death('@F3@'), 'Family ID: @F3@, Result: Error: Death before marriage')

    def test_GED2_family4(self):
        """Testing function on file: Project02.ged"""
        self.assertEqual(GED2.us05_marriage_b4_death('@F4@'), 'Family ID: @F4@, Result: Good')




if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit = False, verbosity= 2)
