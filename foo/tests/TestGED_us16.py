import unittest
import datetime
import sys
import os
from GED import Repository

a = Repository(filename='Project_t16.ged', dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')

class Test_us16_01(unittest.TestCase):
    """Tests conducted on file 'Project_t16.ged'"""

    def test_family_01_01(self):
        """Test us16_male_last_names() for famil 1"""
        self.assertRaises(ValueError, a.us16_male_last_names, '@F1@')

    def test_family_01_02(self):
        """Test us16_male_last_names() for famil 2"""
        self.assertEqual(a.us16_male_last_names('@F2@'), "ID: @F2@, Result: Error: Last names don't match")

    def test_family_01_03(self):
        """Test us16_male_last_names() for famil 3"""
        self.assertEqual(a.us16_male_last_names('@F3@'), "ID: @F3@, Result: Error: Last names don't match")


b = Repository(filename='Project01_Xiaomeng Xu.ged', dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')

class Test_us16_02(unittest.TestCase):
    """Tests conducted on file 'Project01_Xiaomeng Xu.ged'"""

    def test_family_02_01(self):
        """Test us16_male_last_names() for famil 1"""
        self.assertRaises(ValueError, b.us16_male_last_names, '@F1@')

    def test_family_02_02(self):
        """Test us16_male_last_names() for famil 2"""
        self.assertEqual(b.us16_male_last_names('@F2@'), "ID: @F2@, Result: Good")
    
    def test_family_02_03(self):
        """Test us16_male_last_names() for famil 3"""
        self.assertEqual(b.us16_male_last_names('@F3@'), "ID: @F3@, Result: Good")

