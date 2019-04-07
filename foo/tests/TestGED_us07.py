#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Puzhuo Li
@Github: https://github.com/JamesLi0217
@Date: 2019-04-05 23:15:39
'''
# @author: zz2
# Test for us_10
# @update: 2/25/2019

import unittest
import datetime
import os
from GED import Repository
"""
    FOR DEVELOPERS!!!!
    Please make sure that you put this test file in a right directory so that this testing script
    can import things from gedcom.
    Or, change the way how to import modules in this file.
"""


class TestGedcom(unittest.TestCase):
    

    def test_age_less_150(self):
        """
            For developer:
            This test case is for us07
            You do not have to implement T07.01 because it has been implemented in project3 or project 2.
        """
        docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
        a = Repository("Project01_Xiaomeng Xu.ged", os.path.join(docs_dir, 'docs'))
        for people in a.People.values():
            with self.subTest("Individual id: {}".format(people._id)):
                self.assertNotEqual(people._bday, "")
                self.assertNotEqual(people._age, "")
                """
                    To make sure every one has birthday and age.
                """
        self.assertEqual(a.us07_age_less_150('@I2@'), True)
        """
            If the age is more than 150 then should raise a ValueError and print("The age is more than 150")
        """

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
