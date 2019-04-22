#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Puzhuo Li
@Github: https://github.com/JamesLi0217
@Date: 2019-04-05 23:15:39
'''
import unittest
import datetime
import sys
import os
from GED import Repository


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
a = Repository(filename='Project01_Xiaomeng Xu.ged', dir_path=os.path.join(docs_dir, 'docs'))

class Test_us_10_01(unittest.TestCase):
    """Test conducnt on file 'Project01_Xiaomeng Xu.ged"""
    
    def test_family_01(self):
        """Test us10_marriage_after_14() on family 1"""
        self.assertEqual(a.us10_marriage_after_14(), ["ANOMALY: US10: Family@F1@> can't compare if parents are at least 14 years old", "ANOMALY: US10: Family@F2@> can't compare if parents are at least 14 years old"])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit = False, verbosity= 2)
