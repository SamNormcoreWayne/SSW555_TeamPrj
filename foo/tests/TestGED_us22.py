#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Puzhuo Li
@Github: https://github.com/JamesLi0217
@Date: 2019-04-07 01:57:53
'''

import unittest
import sys
import os
from GED import Repository


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
b = Repository(filename='Project01_Xiaomeng Xu.ged',
               dir_path=os.path.join(docs_dir, 'docs'))


class Test_us22_unique_IDs(unittest.TestCase):
    """Tests conducted on file 
    'Project01_Xiaomeng Xu.ged'
    """

    def test_US22_unique_fam_IDs(self):
        """Test us22_unique_fam_IDs()"""
        self.assertEqual(b.us22_unique_fam_IDs(), [])
    
    def test_US22_unique_indi_IDs(self):
        """Test us22_unique_indi_IDs()"""
        self.assertEqual(b.us22_unique_indi_IDs(), [])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
