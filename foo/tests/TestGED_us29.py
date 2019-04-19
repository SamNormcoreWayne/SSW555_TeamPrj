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


class Test_us29_list_deceased(unittest.TestCase):
    """Tests conducted on file 'Project_t23_t24.ged'"""
    a = Repository(filename='Project_t23_t24.ged',
                   dir_path=os.path.join(docs_dir, 'docs'))

    def test_us29_list_deceased(self):
        """Test us29_list_deceased()"""
        self.assertEqual(a.us29_list_deceased(), ['@I8@'])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
