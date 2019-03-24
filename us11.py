#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Puzhuo Li
@Github: https://github.com/JamesLi0217
@Date: 2019-03-22 23:19:15
'''
# @author: XX, ZZ2
# @project holder: PL, ZZ1
"""
    Update: 2019-2-11 13:22:17
    Log:
        creating Individual.add_child()
        creating Individual.add_spouse()
"""

import os
import datetime
from prettytable import PrettyTable
from CheckGED import get_fam, get_indi



class Individual:
    """Repository where we store all information about each person"""

    pt_labels = ['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']

    def __init__(self, id):
        """Initiate a new instance for a individual"""
        self._id = id
        self._name = ''
        self._gender = ''
        self._bday = ''
        self._age = ''
        self._alive = True
        self._dday = 'N/A'
        self._child = 'N/A'
        self._spouse = 'N/A'

    def add_name(self, name):
        """Add person's name to instance"""
        self._name = name

    def add_sex(self, sex):
        """Add gender information to instance"""
        self._gender = sex

    def get_age(self):
        """Calculate individual's age"""
        dt1 = datetime.datetime.strptime(self._bday, '%d %b %Y')
        if not self._alive:
            dt2 = datetime.datetime.strptime(self._dday, '%d %b %Y')
        else:
            dt2 = datetime.datetime.now()

        self._age = ((dt2 - dt1).days) // 365

    def add_bday(self, bday):
        """Add birthday to instace"""
        if bday != '':
            self._bday = bday

    def add_dday(self, dday):
        """Add death infotmation to istance is needed"""
        if dday != '':
            self._alive = False
            self._dday = dday

    def pt_row(self):
        """Return information needed for prettytable"""
        return self._id, self._name, self._gender, self._bday, self._age, self._alive, self._dday, self._child, self._spouse

    def add_child(self, fam_ID):
        if fam_ID != '':
            self._child = fam_ID

    def add_spouse(self, fam_ID):
        if fam_ID != '':
            self._spouse = fam_ID

    def __str__(self):
        """Convert info to string"""
        return f"Individule:{self._id}, name: {self._name}, gender:{self._gender}, bday: {self._bday}, alive: {self._alive}, dday: {self._dday}, age: {self._age}"


class Family():
    def __init__(self, fam_ID, married, divorced, hus, wife, child_id):
        self.fam_ID = fam_ID
        self.mar_date = married
        self.div_date = divorced
        self.hus_id = hus
        self.wife_id = wife
        self.child_id = child_id


class Repository():
    def __init__(self, filename, dir_path=os.getcwd()):
        self.People = dict()
        self.Familis = dict()
        self.working_path = dir_path
        self.filename = filename
        self.read_indi()
        self.read_detail()
        self.input_family()


    def read_indi(self):
        """Read through file, combine information for each person and create a istance of Individual"""
        dd = get_indi(self.working_path, self.filename)
        for i in dd.keys():
            self.People[i] = Individual(i)

    def read_detail(self):
        """Read all detail information for each person, and modify the instaces accordigly"""
        dd = get_indi(self.working_path, self.filename)
        for i in dd.keys():
            for j in range(len(dd[i])):
                if dd[i][j].startswith('1|NAME|'):
                    self.People[i].add_name(dd[i][j].split('|')[3])

                elif dd[i][j].startswith('1|SEX|'):
                    self.People[i].add_sex(dd[i][j].split('|')[3])

                elif dd[i][j].startswith('1|BIRT|'):
                    self.People[i].add_bday(dd[i][j + 1].split('|')[3])

                elif dd[i][j].startswith('1|DEAT|'):
                    self.People[i].add_dday(dd[i][j + 1].split('|')[3])
                elif dd[i][j].startswith('1|FAMS|'):
                    self.People[i].add_spouse(dd[i][j].split('|')[3])
                elif dd[i][j].startswith('1|FAMC|'):
                    self.People[i].add_child(dd[i][j].split('|')[3])
            self.People[i].get_age()

    def individual_pt(self):
        """Create prettytable for all instances of class Individual"""
        pt = PrettyTable(field_names=Individual.pt_labels)
        for i_id in sorted(self.People.keys()):
            pt.add_row(self.People[i_id].pt_row())

        # print('\n', 'Inidividuals')
        # print(pt, '\n')
        return pt.get_string(sortby='ID')

    def input_family(self):
        path = self.working_path
        filename = self.filename
        fam_lst = list(get_fam(path, filename))
        # print("fam_lst: ", fam_lst)
        for fam_dic in fam_lst:
            # print(fam_dic)
            new_family = Family(fam_dic['fam_ID'], fam_dic['mar_date'], fam_dic['div_date'], fam_dic['hus'], fam_dic['wife'], fam_dic['children'])
            self.Familis[fam_dic['fam_ID']] = new_family


    def get_people_name(self, ID):
        for individual in self.People.values():
            if ID == individual._id:
                return individual._name

    def output_family(self):
        field_name = ['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children']
        table = PrettyTable(field_names=field_name)
        hus_name = 'NA'
        wife_name = 'NA'
        for family in self.Familis.values():
            if family.hus_id != 'NA':
                hus_name = self.get_people_name(family.hus_id)
            if family.wife_id != 'NA':
                wife_name = self.get_people_name(family.wife_id)
            table.add_row([family.fam_ID, family.mar_date, family.div_date, family.hus_id, hus_name, family.wife_id, wife_name, family.child_id])

        print(table.get_string(sortby='ID'))
        return table.get_string(sortby='ID')

    #us_03
    def find_indi_ddate(self, indi_id):
        ''' find individual death date by id in family tree'''
        for i in self.People.values():

            if indi_id == i._id:
                if i._dday != 'N/A':
                    return i._dday
                else:
                    return None
                #return i._dday if i._dday != "N/A" else None
        else:
            raise ValueError

    def find_indi_bdate(self, indi_id):
        ''' find individual birth date by id in family tree'''
        for i in self.People.values():

            if indi_id == i._id:
                return i._bday if i._bday != "N/A" else None
        else:
            raise ValueError

    def us03_birth_b4_death(self, indi_id):
        ''' compare individual death date and married date by id in family tree'''

        birth_date = self.find_indi_bdate(indi_id)

        death_date = self.find_indi_ddate(indi_id)

        if death_date == None:
            raise ValueError(f"ID: {indi_id}, Death date not available")
        elif birth_date == None:
            raise ValueError(f"ID: {indi_id}, Birth date not available")
        else:

            #death_date_type = datetime.datetime.strptime(death_date, "%d %b %Y")
            death_date = datetime.datetime.strptime(death_date, "%d %b %Y")
            birth_date = datetime.datetime.strptime(birth_date, "%d %b %Y")

        if death_date < birth_date:
            return f"ID: {indi_id}, Result: Err: Birth before Death"
        else:
            return f"ID: {indi_id}, Result: Good"



    def US11_No_Bigamy(self):
        # orginal edition
        '''for fam_1 in self.Familis:
            for fam_2 in self.Familis:
                if fam_1.fam_ID == fam_2.fam_ID:
                    continue
                if fam_1.hus_id == fam_2.hus_id or fam_1.wife_id == fam_2.wife_id:
                    if fam_1.div_date == 'NA' or fam_2.div_date == 'NA':
                        raise(TypeError('bigamy'))
                    if fam_1.mar_date < fam_2.mar_date:
                        if fam_1.div_date > fam_2.mar_date:
                            raise(TypeError("bigamy"))
                        else:
                            return True'''
        # can't catch Widow
        """for fam_1 in self.Familis.values():
            for fam_2 in self.Familis.values():
                if fam_1.fam_ID != fam_2.fam_ID:
                    if fam_1.hus_id == fam_2.hus_id or fam_1.wife_id == fam_2.wife_id:
                        if fam_1.div_date == 'NA' and fam_2.div_date == 'NA':
                            return 'bigamy'
                        elif fam_1.mar_date < fam_2.mar_date and fam_1.div_date > fam_2.mar_date:
                            return 'bigamy'
        else:
            return True"""
        
        #us_03
        """def find_indi_ddate(self, indi_id):
            ''' find individual death date by id in family tree'''
            for i in self.People.values():

                if indi_id == i._id:
                    if i._dday != 'N/A':
                        return i._dday
                    else:
                        return None
                    #return i._dday if i._dday != "N/A" else None
            else:
                raise ValueError"""
        # final edition: find out all situations that marry normally, then we can know the other part is bigamy.
        for fam_1 in self.Familis.values():
            for fam_2 in self.Familis.values():
                if fam_1.fam_ID != fam_2.fam_ID:
                    if fam_1.hus_id == fam_2.hus_id or fam_1.wife_id == fam_2.wife_id:
                        fam_1_hus_ddate = self.find_indi_ddate(fam_1.hus_id)
                        fam_1_wife_ddate = self.find_indi_ddate(fam_1.wife_id)
                        fam_2.mar_date_dtype = datetime.datetime.strptime(fam_2.mar_date, '%Y-%m-%d')
                        if fam_1.div_date < fam_2.mar_date:
                            return True
                        elif fam_1_hus_ddate:
                            fam_1_hus_ddate_dtype = datetime.datetime.strptime(fam_1_hus_ddate, '%d %b %Y')
                            if fam_1_hus_ddate_dtype < fam_2.mar_date:
                                return True
                        elif fam_1_wife_ddate:
                            fam_1_wife_ddate_dtype = datetime.datetime.strptime(fam_1_wife_ddate, '%d %b %Y')
                            if fam_1_wife_ddate_dtype < fam_2.mar_date_dtype:
                                return True
        else:
            return "bigamy"

def main():
    '''path = input("Input path: ")
    filename = input("Input filename: ")'''
    path=r"D:\sit study\SSW555\PJ"
    filename=r"Project01_Pli.ged"
    rep = Repository(filename=filename, dir_path=path)
    a=rep.individual_pt()
    rep.output_family()
    print(a)
    


if __name__ == "__main__":
    main()
    a=Repository(r"D:\sit study\SSW555\PJ\Project01_Pli.ged")
    result=a.US11_No_Bigamy()
    print(result)
