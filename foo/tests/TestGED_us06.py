'''
@Author: Puzhuo Li
@Github: https://github.com/JamesLi0217
@Date: 2019-02-16 21:07:16
'''


import os
import unittest
from GED import Individual, Repository
#from HW04_pli import store_divorce_date,store_death_date,test_us_06_compare_divrdate_ddate


'''US06	Divorce before death'''
docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
a = Repository(filename = "Project01_Xiaomeng Xu.ged", dir_path = os.path.join(docs_dir, 'docs'))
class TestGED(unittest.TestCase):
    '''test store_divorce_date() ,store_death_date() and us_06_compare_divrdate_ddate()'''

    def test_store_divorce_date(self):
        '''test store_divorce_date()'''
        #a = Repository("Project01_Xiaomeng Xu.ged", os.path.join(os.getcwd(), 'docs'))
        self.assertEqual(a.store_divorce_date("@F3@"),"1980-05-06") # 幸福美满的家庭没有离婚的情况。。。
        self.assertIsNone(a.store_divorce_date("@F4@")) # indi_id exist but death date doesn't exist return None
        with self.assertRaises(ValueError): # divr date doesn't exist -->raise valueError
            a.store_divorce_date("@F8@")

    def test_store_death_date(self):
        '''test store_death_date()'''
        #a = Repository("Project01_Xiaomeng Xu.ged", os.path.join(os.getcwd(), 'docs'))
        self.assertIsNone(a.store_death_date("@I4@")) # indi_id exist but death date doesn't exist return None
        self.assertEqual(a.store_death_date("@I2@"),"14 MAR 2001")
        with self.assertRaises(ValueError): # indi_id doesn't exist raise valueError
            a.store_death_date("@I8@")

    def test_us_06_compare_divrdate_ddate(self):
        '''test us_06_compare_divrdate_ddate()'''
        #a = Repository("Project01_Xiaomeng Xu.ged", os.path.join(os.getcwd(), 'docs'))
        self.assertTrue(a.us_06_compare_divrdate_ddate("@F3@", "@I2@", "@I3@")) # death date is later than divorce 同样幸福美满没有离婚的
        with self.assertRaises(ValueError): # death date or divr date doesn't exist -->raise valueError
            a.us_06_compare_divrdate_ddate("@F4@", "@I1@", "@I4@")

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
