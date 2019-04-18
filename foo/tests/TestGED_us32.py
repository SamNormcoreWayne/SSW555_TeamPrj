import unittest
import datetime
import sys
import os
from GED import Repository

docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
a = Repository(filename='what_a_mass.ged', dir_path=os.path.join(docs_dir, 'docs'))

class Test_us32_a(unittest.TestCase):
    """Tests conducted on file 'what_a_mass.ged'"""

    def test_us32_a(self):
        """Test us32_list_all_multiple_births()"""
        self.assertEqual(a.us32_list_all_multiple_births(), {['@F3@', '@F4@']})

b = Repository(filename='Project01_Xiaomeng Xu.ged', dir_path=os.path.join(docs_dir, 'docs'))

class Test_us32_b(unittest.TestCase):
    """Tests conducted on file 'Project01_Xiaomeng Xu.ged'"""

    def test_us32_b(self):
        """Test us32_list_all_multiple_births()"""
        self.assertEqual(b.us32_list_all_multiple_births(), {[]})


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
