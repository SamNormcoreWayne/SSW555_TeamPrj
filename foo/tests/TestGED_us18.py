#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Puzhuo Li
@Github: https://github.com/JamesLi0217
@Date: 2019-04-07 00:44:34
'''
import unittest
import sys
import os
from GED import Repository


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
a = Repository(filename='Project01_Xiaomeng Xu.ged',
               dir_path=os.path.join(docs_dir, 'docs'))


class Test_us18_Siblings_should_not_marry(unittest.TestCase):
    """Tests conducted on file 
    'Project_t17.ged'

    """

    def test_US18_Siblings_should_not_marry(self):
        """Test us18_Siblings_should_not_marry()"""
        self.assertEqual(a.us18_Siblings_should_not_marry(), [
                         'ERROR: US18: FAMILY @F3@ marriages'])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
