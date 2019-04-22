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
        self.assertEqual(b.US11_No_Bigamy(), ['Error: US11: FAMILY<@F1@> husband @I1@ has more than 1 spounse during marriage in family @F2@!',
                                              'Error: US11: FAMILY<@F1@> husband @I1@ has more than 1 spounse during marriage in family @F4@!'])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
