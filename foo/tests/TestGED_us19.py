import unittest
import datetime
import sys
import os
from GED import Repository


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
a = Repository(filename='Project01_Xiaomeng Xu.ged', dir_path=os.path.join(docs_dir, 'docs'))

class TestUS19(unittest.TestCase):
    def test_us19_cousins_not_marry(self):
        self.assertEqual(a.us_19_cousins_not_marry("@I1@"), True)
        with self.assertRaises(ValueError):
            a.us_19_cousins_not_marry("@I84@")
