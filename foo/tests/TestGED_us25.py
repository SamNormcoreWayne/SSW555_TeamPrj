import unittest
import datetime
import sys
import os
from GED import Repository


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
a = Repository(filename='Project_t23_t24.ged', dir_path=os.path.join(docs_dir, 'docs'))


class TestUS25(unittest.TestCase):
    def test_us25_unique_children(self):
        self.assertEqual(a.us25_unique_first_name(), False)