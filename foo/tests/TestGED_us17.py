#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Puzhuo Li
@Github: https://github.com/JamesLi0217
@Date: 2019-04-07 00:44:27
'''
import unittest
import sys
import os
from GED import Repository


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
a= Repository(filename='Project_t17.ged',
               dir_path=os.path.join(docs_dir, 'docs'))



class Test_us17_No_marriages_to_children(unittest.TestCase):
    """Tests conducted on file 
    'Project_t17.ged'

    """

    def test_US17_No_marriages_to_children(self):
        """Test us17_sibling_spacing()"""
        self.assertEqual(a.us17_No_marriages_to_children(),)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)