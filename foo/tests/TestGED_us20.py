import unittest
import datetime
import sys
import os
from GED import Repository


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
a = Repository(filename='Project01_Xiaomeng Xu.ged', dir_path=os.path.join(docs_dir, 'docs'))

class TestUS20(unittest.TestCase):
    def test_us20_aunts_uncle(self):
        with self.assertRaises(KeyError):
            self.assertTrue(a.us20_aunts_uncle("@I1@"))
        with self.assertRaises(ValueError):
            a.us20_aunts_uncle("@I234@")