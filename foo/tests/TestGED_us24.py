import unittest
import datetime
import sys
import os
from GED import Repository


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
a = Repository(filename='Project_t23_t24.ged', dir_path=os.path.join(docs_dir, 'docs'))

class Test_us24_a(unittest.TestCase):
    """Tests conducted on file 'Project_t23_t24.ged'"""

    def test_us24_a(self):
        """Test us24_unique_family_by_spouse()"""
        self.assertEqual(a.us24_unique_family_by_spouse(), {'@F4@', '@F7@'})

b = Repository(filename='Project01_Xiaomeng Xu.ged', dir_path=os.path.join(docs_dir, 'docs'))

class Test_us24_b(unittest.TestCase):
    """Tests conducted on file 'Project01_Xiaomeng Xu.ged'"""

    def test_us24_b(self):
        """Test us24_unique_family_by_spouse()"""
        self.assertEqual(b.us24_unique_family_by_spouse(), set())


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
