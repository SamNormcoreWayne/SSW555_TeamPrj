#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Puzhuo Li
@Github: https://github.com/JamesLi0217
@Date: 2019-04-18 22:00:22
'''
import unittest
import datetime
import sys
import os
from GED import Repository


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))


class Test_us27_include_individual_ages(unittest.TestCase):
    """Tests conducted on file 'Project_t27_29.ged'"""
    a = Repository(filename='Project_t27_29.ged',
                   dir_path=os.path.join(docs_dir, 'docs'))

    def test_us27_include_individual_ages(self):
        """Test us27_include_individual_ages()"""
        self.assertEqual(a.us27_include_individual_ages(), ['@I1@', '@I2@', '@I3@'])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
