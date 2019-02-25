# @author: zz2
# Test for us_10
# @update: 2/25/2019

import unittest
import datetime
from GED import Repository
"""
    FOR DEVELOPERS!!!!
    Please make sure that you put this test file in a right directory so that this testing script
    can import things from gedcom.
    Or, change the way how to import modules in this file.
"""


class TestGedcom(unittest.TestCase):
    '''
    @classmethod
    def setUpClass(cls):
        sys.path.append(os.path.dirname(os.getcwd()))
        from gedcom import Repository
        print("Test starts")
    
    @classmethod
    def tearDownClass(cls):
        print("Test ends.")
    '''

    """def test_birth_b4_now(self):
        '''
            This a test case for us04. If you are working on us10, please ignore this test case. 
        '''
        a = Repository("Project01_Xiaomeng Xu.ged", r'/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')
        result = datetime.datetime.strptime(a.us_01_birth_b4_now(), "%d %b %Y")
        current_time = datetime.datetime.now()
        for people in a.People:
            with self.subTest():
                self.assertFalse(people._bday, "")
                self.assertFalse(people.dday, "")
        self.assertLess((result - current_time).days, 0)
        self.assertGreater((current_time - result).days, 0)
        with self.assertRaises(TypeError):
            datetime.datetime.strftime(result)
        self.assertTrue((current_time - result).days > 0)
        self.assertFalse((current_time - result).days < 0)"""

    def test_age_less_150(self):
        """
            For developer:
            This test case is for us07
            You do not have to implement T07.01 because it has been implemented in project3 or project 2.
        """
        a = Repository("Project01_Xiaomeng Xu.ged", '/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')
        for people in a.People.values():
            with self.subTest("Individual id: {}".format(people._id)):
                self.assertNotEqual(people._bday, "")
                self.assertNotEqual(people._age, "")
                """
                    To make sure every one has birthday and age.
                """
        self.assertEqual(a.us07_age_less_150('@I2@'), True)
        """
            If the age is more than 150 then should raise a ValueError and print("The age is more than 150")
        """

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
