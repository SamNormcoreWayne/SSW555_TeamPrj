import unittest
import datetime
from gedcom import Repository


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

    def test_birth_b4_now(self):
        a = Repository(filename='Project01_Xiaomeng Xu.ged', dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')
        current_time = datetime.datetime.now()
        for result in a.us_01_birth_b4_now():
            with self.subTest():
                self.assertLess((result - current_time).days, 0)
                self.assertGreater((current_time - result).days, 0)
                self.assertTrue((current_time - result).days > 0)
                self.assertFalse((current_time - result).days < 0)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)