import unittest
import datetime
import sys
import os
from GED import Repository

docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
a = Repository(filename='what_a_mass.ged', dir_path=os.path.join(docs_dir, 'docs'))

class Test_us26_a(unittest.TestCase):
    """Tests conducted on file 'what_a_mass.ged'"""

    def test_us26_a(self):
        """Test us26_corresponding_entries()"""
        self.assertEqual(a.us26_corresponding_entries(), {['@I13@', '@I16@']})


b = Repository(filename='Project01_Xiaomeng Xu.ged', dir_path=os.path.join(docs_dir, 'docs'))

class Test_us26_b(unittest.TestCase):
    """Tests conducted on file 'Project01_Xiaomeng Xu.ged'"""

    def test_us26_b(self):
        """Test us26_corresponding_entries()"""
        self.assertEqual(b.us26_corresponding_entries(), {[]})


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
