#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Puzhuo Li
@Github: https://github.com/JamesLi0217
@Date: 2019-03-23 21:55:01
'''
import unittest
import sys
import os
from GED import Repository


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
b = Repository(filename='Project01_Xiaomeng Xu.ged',
               dir_path=os.path.join(docs_dir, 'docs'))


class Test_us21_correct_gender(unittest.TestCase):
    """Tests conducted on file 
    'Project01_Xiaomeng Xu.ged'
    """

    def test_US21_correct_gender(self):
        """Test us21_correct_gender()"""
        self.assertEqual(b.us21_correct_gender(), ["ANOMALY: US21: Family@F1@> can't compare if the roles of parents are correct"])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
