import unittest
import datetime
import sys
import os
from GED import Repository


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))


class Test_us27_include_individual_ages(unittest.TestCase):
    """Tests conducted on file 'Project_t23_t24.ged'"""
    a = Repository(filename='Project_t23_t24.ged',
                   dir_path=os.path.join(docs_dir, 'docs'))

    def test_us27_include_individual_ages(self):
        """Test us27_include_individual_ages()"""
        self.assertEqual(a.us27_include_individual_ages(), {'@F4@', '@F7@'})


    b = Repository(filename='Project01_Xiaomeng Xu.ged',
                   dir_path=os.path.join(docs_dir, 'docs'))

    def test_us27_include_individual_ages(self):
        """Test us27_include_individual_ages()"""
        self.assertEqual(b.us27_include_individual_ages(), set())


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
