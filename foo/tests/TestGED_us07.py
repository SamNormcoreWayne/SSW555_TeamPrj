#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Puzhuo Li
@Github: https://github.com/JamesLi0217
@Date: 2019-04-05 23:15:39
'''
# @author: zz2
# Test for us_10
# @update: 2/25/2019

import unittest
import datetime
import os
from GED import Repository
"""
    FOR DEVELOPERS!!!!
    Please make sure that you put this test file in a right directory so that this testing script
    can import things from gedcom.
    Or, change the way how to import modules in this file.
"""


class TestGedcom(unittest.TestCase):

    def test_age_less_150(self):
        """
            This test case is for us07
        """
        docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
        a = Repository("Project01_Xiaomeng Xu.ged",
                       os.path.join(docs_dir, 'docs'))

        self.assertEqual(a.us07_age_less_150(), [
                         "ANOMALY: US07: Individual@I7@> didn't record age"])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
