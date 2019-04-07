#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Puzhuo Li
@Github: https://github.com/JamesLi0217
@Date: 2019-04-07 00:23:29
'''
import unittest
import os
from GED import Repository


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
GED1 = Repository(filename='Project_t03.ged',
                  dir_path=os.path.join(docs_dir, 'docs'))


class Test_us04_marriage_b4_divoce(unittest.TestCase):
    """These are test cases for user story 04: Check if a family's marriage date is before divoce date(if available)"""
    # Test cases for US_04

    def test_GED2_family1(self):
        """Testing function on file: Project_t04.ged"""
        self.assertEqual(GED1.us04_marriage_b4_divoce(), ['ANOMALY: US04: FAMILY:<@F1@> No marriage date',
                                                          'ERROR: US04: FAMILY:<@F2@> Divoce before Marriage', 'ERROR: US04: FAMILY:<@F3@> Divoce before Marriage'])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
