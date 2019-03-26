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
c = Repository(filename='Project02.ged',
               dir_path=os.path.join(docs_dir, 'docs'))
d = Repository(filename='Project_t03.ged',
               dir_path=os.path.join(docs_dir, 'docs'))
e = Repository(filename='Project_t04.ged',
               dir_path=os.path.join(docs_dir, 'docs'))
f = Repository(filename='Project_t10.ged',
               dir_path=os.path.join(docs_dir, 'docs'))
# g = Repository(filename='Project01_us12_Pli.ged',
               # dir_path=os.path.join(docs_dir, 'docs'))

class Test_us12_01(unittest.TestCase):
    """Tests conducted on file 
    'Project01_Pli.ged'
    'Project01_Xiaomeng Xu.ged'
    'Project02.ged'
    'Project_t03.ged'
    'Project_t04.ged'
    'Project_t10.ged'
    'Project01_us12_Pli.ged'
    """

    def test_us12_parents_not_2_old(self):
        """Test us12_parents_not_2_old()"""

        self.assertTrue(b.us12_parents_not_2_old())
        self.assertTrue(c.us12_parents_not_2_old())
        self.assertTrue(d.us12_parents_not_2_old())
        self.assertTrue(e.us12_parents_not_2_old())
        self.assertTrue(f.us12_parents_not_2_old())
        # with self.assertRaises(TypeError):
            # g.us12_parents_not_2_old()


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
