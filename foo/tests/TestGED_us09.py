#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Puzhuo Li
@Github: https://github.com/JamesLi0217
@Date: 2019-04-05 23:15:39
'''
import unittest
import datetime
import sys
import os
from GED import Repository


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
a = Repository(filename='Project01_Xiaomeng Xu.ged',
               dir_path=os.path.join(docs_dir, 'docs'))


class TestUS09(unittest.TestCase):
    def test_us09_birth_b4_parents_death(self):
        self.assertTrue(a.us09_birth_b4_parents_death(), ["ANOMALY: US09: Individual@I2@> Can't compare birth date and parents' death date", "ANOMALY: US09: Individual@I3@> Can't compare birth date and parents' death date", "ANOMALY: US09: Individual@I4@> Can't compare birth date and parents' death date", "ANOMALY: US09: Individual@I5@> Can't compare birth date and parents' death date", "ANOMALY: US09: Individual@I6@> Can't compare birth date and parents' death date", "ANOMALY: US09: Individual@I7@> Can't compare birth date and parents' death date"])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
