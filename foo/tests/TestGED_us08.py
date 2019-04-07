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


class TestUS08(unittest.TestCase):
    def test_us08_birth_b4_parents_marriage(self):
        self.assertTrue(a.us08_birth_b4_parents_marriage(), ['ERROR: US08: Individual@I1@> Birth date is before Marriage', "ANOMALY: US08: Individual@I2@> Can't compare marriage date and divorce date", "ANOMALY: US08: Individual@I3@> Can't compare marriage date and divorce date",
                                                             "ANOMALY: US08: Individual@I4@> Can't compare marriage date and divorce date", "ANOMALY: US08: Individual@I5@> Can't compare marriage date and divorce date", 'ERROR: US08: Individual@I6@> Birth date is before Marriage', 'ERROR: US08: Individual@I7@> Birth date is before Marriage'])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
