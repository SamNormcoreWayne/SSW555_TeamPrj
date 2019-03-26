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


a= Repository(filename='Project01_Xiaomeng Xu.ged',
               dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')



class Test_us13_01(unittest.TestCase):
    """Tests conducted on file 
    'Project01_Xiaomeng Xu.ged'

    """

    def test_US13_sibling_spacing(self):
        """Test us13_sibling_spacing()"""
        self.assertTrue(a.us13_sibling_spacing("F1"))
        self.assertTrue(a.us13_sibling_spacing("F2"))
        self.assertTrue(a.us13_sibling_spacing("F3"))
        self.assertTrue(a.us13_sibling_spacing("F4"))
        with self.assertRaises(KeyError):
            a.us13_sibling_spacing("F5")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)