"""SSW555_Sprint01_US03_US04_Test
    Xiaomeng Xu"""

import unittest
import os
from GED import Repository


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
GED1 = Repository(filename='Project_t03.ged', dir_path=os.path.join(docs_dir, 'docs'))
GED2 = Repository(filename='Project_t04.ged', dir_path=os.path.join(docs_dir, 'docs'))
class Test_us03_birth_b4_death(unittest.TestCase):
    """This are the test cases for user story_03: check if a individual's birth date is before death date."""
    #Test cases for US_03
    def test_GED1_individual1(self):
        """Testing function on file: Project_t03.ged"""
        self.assertRaises(ValueError, GED1.us03_birth_b4_death, '@I1@')
    
    def test_GED1_individual2(self):
        """Testing function on file: Project_t03.ged"""
        self.assertEqual(GED1.us03_birth_b4_death('@I2@'), 'ID: @I2@, Result: Err: Birth before Death')
    
    def test_GED1_individual3(self):
        """Testing function on file: Project_t03.ged"""
        self.assertEqual(GED1.us03_birth_b4_death('@I3@'), 'ID: @I3@, Result: Good')
    
    def test_GED1_individual4(self):
        """Testing function on file: Project_t03.ged"""
        self.assertRaises(ValueError, GED1.us03_birth_b4_death, '@I4@')

    def test_GED1_individual5(self):
        """Testing function on file: Project_t03.ged"""
        self.assertEqual(GED1.us03_birth_b4_death('@I5@'), 'ID: @I5@, Result: Err: Birth before Death')

    def test_GED1_individual6(self):
        """Testing function on file: Project_t03.ged"""
        self.assertRaises(ValueError, GED1.us03_birth_b4_death, '@I6@')

    def test_GED1_individual7(self):
        """Testing function on file: Project_t03.ged"""
        self.assertRaises(ValueError, GED1.us03_birth_b4_death, '@I7@')
    


class Test_us04_marriage_b4_divoce(unittest.TestCase):
    """These are test cases for user story 04: Check if a family's marriage date is before divoce date(if available)"""
    #Test cases for US_04
    def test_GED2_family1(self):
        """Testing function on file: Project_t04.ged"""
        self.assertEqual(GED2.us04_marriage_b4_divoce('@F1@'), 'ID: @F1@, Result: No marriage date')

    def test_GED2_family2(self):
        """Testing function on file: Project_t04.ged"""
        self.assertEqual(GED2.us04_marriage_b4_divoce('@F2@'), 'ID: @F2@, Result: Err: Divoce before Marriage')

    def test_GED2_family3(self):
        """Testing function on file: Project_t04.ged"""
        self.assertEqual(GED2.us04_marriage_b4_divoce('@F3@'), 'ID: @F3@, Result: Err: Divoce before Marriage')

    def test_GED2_family4(self):
        """Testing function on file: Project_t04.ged"""
        self.assertEqual(GED2.us04_marriage_b4_divoce('@F4@'), 'ID: @F4@, Result: No divoce date')




if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit = False, verbosity= 2)
