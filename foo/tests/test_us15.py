import unittest
import sys
import os
from GED import Repository

a = Repository(filename='Project01_Pli.ged',
               dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')
b = Repository(filename='Project01_Xiaomeng Xu.ged',
               dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')
c = Repository(filename='Project02.ged',
               dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')
d = Repository(filename='Project_t03.ged',
               dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')
e = Repository(filename='Project_t04.ged',
               dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')
f = Repository(filename='Project_t10.ged',
               dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')
g = Repository(filename='Project_t16.ged',
               dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')
h = Repository(filename='Project_t15.ged',
               dir_path='/home/travis/build/SamNormcoreWayne/SSW555_TeamPrj/docs')


class Test_us15_(unittest.TestCase):
    """Tests conducted on file
    'Project01_Pli.ged'
    'Project01_Xiaomeng Xu.ged'
    'Project02.ged'
    'Project_t03.ged'
    'Project_t04.ged'
    'Project_t10.ged'
    'Project_t16.ged'
    """

    def test_us15(self):
        'Test no more than 15 children in a family'
        self.assertTrue(a.US15_Fewer_15_Child())
        self.assertTrue(b.US15_Fewer_15_Child())
        self.assertTrue(c.US15_Fewer_15_Child())
        self.assertTrue(d.US15_Fewer_15_Child())
        self.assertTrue(e.US15_Fewer_15_Child())
        self.assertTrue(f.US15_Fewer_15_Child())
        self.assertTrue(g.US15_Fewer_15_Child())
        self.assertTrue(h.US15_Fewer_15_Child())


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
