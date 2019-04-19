import unittest
import datetime
import sys
import os
from GED import Repository


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
a = Repository(filename='what_a_mass.ged',
               dir_path=os.path.join(docs_dir, 'docs'))


class Test_us31_list_living_single(unittest.TestCase):
    """Tests conducted on file 'what_a_mass.ged'"""

    def test_us31_list_living_single(self):
        """Test us31_list_living_single()"""
        self.assertEqual(a.us31_list_living_single(), [])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
