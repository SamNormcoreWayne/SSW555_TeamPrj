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

a = Repository(filename='Project01_Pli.ged',
               dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')
b = Repository(filename='Project01_Xiaomeng Xu.ged',
               dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')
c = Repository(filename='Project02.ged',
               dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')
d = Repository(filename='Project_t03.ged',
               dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')
e = Repository(filename='Project_t04.ged',
               dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')
f = Repository(filename='Project_t10.ged',
               dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')
g = Repository(filename='Project_t16.ged',
               dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')


class Test_us11_01(unittest.TestCase):
    """Tests conducted on file 
    'Project01_Pli.ged'
    'Project01_Xiaomeng Xu.ged'
    'Project02.ged'
    'Project_t03.ged'
    'Project_t04.ged'
    'Project_t10.ged'
    'Project_t16.ged'
    """

    def test_US11_No_Bigamy(self):
        """Test US11_No_Bigamy()"""
        self.assertTrue(a.US11_No_Bigamy())
        self.assertTrue(b.US11_No_Bigamy())
        self.assertTrue(c.US11_No_Bigamy())
        self.assertTrue(d.US11_No_Bigamy())
        self.assertTrue(e.US11_No_Bigamy())
        self.assertTrue(f.US11_No_Bigamy())
        self.assertTrue(g.US11_No_Bigamy())


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
