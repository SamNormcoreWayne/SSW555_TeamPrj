#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Puzhuo Li
@Github: https://github.com/JamesLi0217
@Date: 2019-04-05 23:15:39
'''
import unittest
import os
from GED import Repository

docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

a = Repository(filename='Project01_Pli.ged',
               dir_path=os.path.join(docs_dir, 'docs'))
h = Repository(filename='Project_t15.ged',
               dir_path=os.path.join(docs_dir, 'docs'))


class Test_us15_(unittest.TestCase):
    """Tests conducted on file
    'Project01_Pli.ged'
    'Project01_Xiaomeng Xu.ged'
    'Project02.ged'
    'Project_t03.ged'
    'Project_t04.ged'
    'Project_t10.ged'
    'Project_t16.ged'
    'Peoject_t15.ged'  #have 18 children in a family
    """

    def test_us15(self):
        'Test no more than 15 children in a family'
        self.assertEqual(h.US15_Fewer_15_Child(), [
                         'Error: US15: FAMILY<@F3@> has more than 15 children!'])
        self.assertEqual(a.US15_Fewer_15_Child(), [])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
