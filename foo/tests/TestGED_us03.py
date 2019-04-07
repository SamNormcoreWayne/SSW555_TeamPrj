#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Puzhuo Li
@Github: https://github.com/JamesLi0217
@Date: 2019-04-05 23:15:39
'''
"""SSW555_Sprint01_US03_US04_Test
    Xiaomeng Xu"""

import unittest
import os
from GED import Repository


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
GED1 = Repository(filename='Project_t03.ged',
                  dir_path=os.path.join(docs_dir, 'docs'))


class Test_us03_birth_b4_death(unittest.TestCase):
    """This are the test cases for user story_03: check if a individual's birth date is before death date."""
    # Test cases for US_03

    def test_GED1_individual1(self):
        """Testing function on file: Project_t03.ged"""
        self.assertRaises(['ERROR: US03: Individual@I2@> birth date is after death date',
                           'ERROR: US03: Individual@I5@> birth date is after death date'], GED1.us03_birth_b4_death())


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
