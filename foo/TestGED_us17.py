#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Puzhuo Li
@Github: https://github.com/JamesLi0217
@Date: 2019-04-07 00:44:27
'''
import unittest
import sys
import os
from GED import Repository


docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
a = Repository(filename='Project_t17.ged',dir_path=os.path.join(docs_dir, 'docs'))
'''path = r"/Users/daiyuping/Documents/GitHub/SSW555_TeamPrj/docs"
filename = r"Project_t17.ged"
a = Repository(filename=filename, dir_path=path)'''

class Test_us17_No_marriages_to_children(unittest.TestCase):
    """Tests conducted on file 
    'Project_t17.ged'

    """

    def test_US17_No_marriages_to_children(self):
        """Test No_marriages_to_children()"""
        self.assertEqual(a.us17_No_marriages_to_children(), [
                         "ERROR: US17: FAMILY @F5@ father @I7@> marriages to children ['@I7@']"])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
    '''path = r"/Users/daiyuping/Documents/GitHub/SSW555_TeamPrj/docs"
    filename = r"Project_t17.ged"
    a = Repository(filename=filename, dir_path=path)
    b=a.us17_No_marriages_to_children()
    print(b)'''