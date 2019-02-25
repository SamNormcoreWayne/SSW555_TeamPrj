import unittest
import datetime
import sys
import os
from GED import Repository


a = Repository(filename='Project01_Xiaomeng Xu.ged', dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')
b = Repository(filename='Project_t10.ged', dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')

class Test_us_10_01(unittest.TestCase):
    """Test conducnt on file 'Project01_Xiaomeng Xu.ged"""
    
    def test_family_01(self):
        """Test us10_marriage_after_14() on family 1"""
        self.assertEqual(a.us10_marriage_after_14('@F1@'), 'ID: @F1@, Result: No Marriage date')
    
    def test_family_02(self):
        """Test us10_marriage_after_14() on family 2"""
        self.assertEqual(a.us10_marriage_after_14('@F2@'), 'ID: @F2@, Result: No Marriage date')
    
    def test_family_03(self):
        """Test us10_marriage_after_14() on family 3"""
        self.assertEqual(a.us10_marriage_after_14('@F3@'), 'ID: @F3@, Result: Good')

    def test_family_04(self):
        """Test us10_marriage_after_14() on family 4"""
        self.assertEqual(a.us10_marriage_after_14('@F4@'), 'ID: @F4@, Result: Good')

class Test_us_10_02(unittest.TestCase):
    """Test conducnt on file 'Project_t10.ged"""
    
    def test_family_01(self):
        """Test us10_marriage_after_14() on family 1"""
        self.assertEqual(b.us10_marriage_after_14('@F1@'), 'ID: @F1@, Result: No Marriage date')
    
    def test_family_02(self):
        """Test us10_marriage_after_14() on family 2"""
        self.assertEqual(b.us10_marriage_after_14('@F2@'), 'ID: @F2@, Result: Good')
    
    def test_family_03(self):
        """Test us10_marriage_after_14() on family 3"""
        self.assertEqual(b.us10_marriage_after_14('@F3@'), 'ID: @F3@, Result: ERROR')

    def test_family_04(self):
        """Test us10_marriage_after_14() on family 4"""
        self.assertEqual(b.us10_marriage_after_14('@F4@'), 'ID: @F4@, Result: ERROR')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit = False, verbosity= 2)
