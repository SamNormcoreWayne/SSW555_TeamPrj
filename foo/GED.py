#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Puzhuo Li
@Github: https://github.com/JamesLi0217
@Date: 2019-02-26 18:00:26
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
from collections import defaultdict


class Individual:
    """Repository where we store all information about each person"""

    pt_labels = ['ID', 'Name', 'Gender', 'Birthday',
                 'Age', 'Alive', 'Death', 'Child', 'Spouse']

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

        print('\n', 'Inidividuals')
        print(pt, '\n')
        return pt.get_string(sortby='ID')

    def input_family(self):
        path = self.working_path
        filename = self.filename
        fam_lst = list(get_fam(path, filename))
        # print("fam_lst: ", fam_lst)
        for fam_dic in fam_lst:
            # print(fam_dic)
            new_family = Family(fam_dic['fam_ID'], fam_dic['mar_date'], fam_dic['div_date'],
                                fam_dic['hus'], fam_dic['wife'], fam_dic['children'])
            self.Familis[fam_dic['fam_ID']] = new_family

    def getPeople(self, ID):
        for ind_ID, individual in self.People.items():
            # print(ind_ID, individual._id, ID)
            if ind_ID == ID:
                return individual

    '''
    def getPeople_id(self, name):
        for individual in self.People.values():
            if name == individual._name:
                return individual._id
    '''

    def get_people_name(self, ID):
        for individual in self.People.values():
            if ID == individual._id:
                return individual._name

    def output_family(self):
        field_name = ['ID', 'Married', 'Divorced', 'Husband ID',
                      'Husband Name', 'Wife ID', 'Wife Name', 'Children']
        table = PrettyTable(field_names=field_name)
        hus_name = 'NA'
        wife_name = 'NA'
        for family in self.Familis.values():
            if family.hus_id != 'NA':
                hus_name = self.get_people_name(family.hus_id)
            if family.wife_id != 'NA':
                wife_name = self.get_people_name(family.wife_id)
            table.add_row([family.fam_ID, family.mar_date, family.div_date,
                           family.hus_id, hus_name, family.wife_id, wife_name, family.child_id])

        print('Families')
        print(table.get_string(sortby='ID'))
        return table.get_string(sortby='ID')

    # us_01
    def us_01_birth_b4_now(self):
        for person in self.People.values():
            bd = datetime.datetime.strptime(person._bday, '%d %b %Y')
            if bd > datetime.datetime.now():
                yield("ERROR: INDIVIDUAL: us01: {id} is not born".format(id=person._id))
            else:
                yield bd

    # us_02
    def us02_birth_b4_marriage(self):
        """For a givenn fam_id, check the family marriage date and birthday for each individual, retuen the result"""
        result = []
        for fam_id in self.Familis.keys():
            if self.Familis[fam_id].mar_date != 'NA' and self.Familis[fam_id].child_id != ['NA']:

                mdt = datetime.datetime.strptime(
                    self.Familis[fam_id].mar_date, '%Y-%m-%d')
                for child_id in self.Familis[fam_id].child_id:
                    if self.People[child_id]._bday == 'N/A':
                        continue
                    else:
                        bdt = datetime.datetime.strptime(
                            self.People[child_id]._bday, '%d %b %Y')
                        if bdt < mdt:
                            print(f"ANOMALY: FAMILY:<{fam_id}>, US02: Child<{child_id}> born {bdt} before marriage on {mdt}")
                            result.append(f"ANOMALY: FAMILY:<{fam_id}>")
        
        #print(result)
        return result
 
                


    # us_03

    def find_indi_ddate(self, indi_id):
        ''' find individual death date by id in family tree'''
        for i in self.People.values():

            if indi_id == i._id:
                if i._dday != 'N/A':
                    return i._dday
                else:
                    return None
                # return i._dday if i._dday != "N/A" else None
        '''else:
            raise ValueError'''

    def find_indi_bdate(self, indi_id):
        ''' find individual birth date by id in family tree'''
        for i in self.People.values():

            if indi_id == i._id:
                return i._bday if i._bday != "N/A" else None
        else:
            raise ValueError

    def us03_birth_b4_death(self):
        ''' compare individual death date and married date by id in family tree'''
        result_list = []
        for indi_id in self.People:
            birth_date = self.find_indi_bdate(indi_id)

            death_date = self.find_indi_ddate(indi_id)

            if birth_date is None:
                print(
                    f"ANOMALY: US03: Individual{indi_id}> doesn't have birth date")
                result_list.append(f"ANOMALY: US03: Individual{indi_id}> doesn't have birth date")
            elif death_date:
                death_date = datetime.datetime.strptime(death_date, "%d %b %Y")
                birth_date = datetime.datetime.strptime(birth_date, "%d %b %Y")
                if death_date < birth_date:
                    print(f"ERROR: US03: Individual{indi_id}> birth date is after death date")
                    result_list.append(f"ERROR: US03: Individual{indi_id}> birth date is after death date")
        return result_list

    # us_04

    def us04_marriage_b4_divoce(self):
        """Compare marriage date and divoce date(if available) for each family"""
        result_list = []

        for fam_id in self.Familis:
            mar_date = self.Familis[fam_id].mar_date
            div_date = self.Familis[fam_id].div_date
            if mar_date == 'NA':
                print(f"ANOMALY: US04: FAMILY:<{fam_id}> No marriage date")
                result_list.append(f"ANOMALY: US04: FAMILY:<{fam_id}> No marriage date")
            elif div_date != 'NA':
                mar_dt = datetime.datetime.strptime(mar_date, "%Y-%m-%d")
                div_dt = datetime.datetime.strptime(div_date, "%Y-%m-%d")
                if mar_dt > div_dt:  # Check if marriage date comes after divoce date
                    print(f"ERROR: US04: FAMILY:<{fam_id}> Divoce before Marriage")
                    result_list.append(f"ERROR: US04: FAMILY:<{fam_id}> Divoce before Marriage")
        return result_list

    # us_05
    def us05_marriage_b4_death(self):
        """For a given fam_id, check the family marriage date and death date for each individual belongs to this family, return the result of checking"""
        result = []
        for fam_id in self.Familis.keys():

            if self.Familis[fam_id].mar_date != 'NA':
                # If there is marriage date, covert it to datetime object
                mdt = datetime.datetime.strptime(
                    self.Familis[fam_id].mar_date, '%Y-%m-%d')
                ddates = {}
                hus_id = self.Familis[fam_id].hus_id
                wife_id = self.Familis[fam_id].wife_id
                # Get husband's death date in ddate, coule be 'N/A'
                ddates[hus_id] = self.People[hus_id]._dday
                # Get wife's death date in ddate, could be 'N/A'
                ddates[wife_id] = self.People[wife_id]._dday
                for key, value in ddates.items():
                    # Check elements in ddate, if there is a death date, compare it with marriage date(mdt), if death date was before marriage date, change reuslt and break out of loop
                    if value != 'N/A':
                        ddt = datetime.datetime.strptime(value, '%d %b %Y')
                        if ddt < mdt:
                            print(f"ERROR: FAMILY:<{fam_id}>, US05: Individule<{key}> die on {ddt} before marriage on {mdt}")
                            result.append(f"ERROR: FAMILY:<{fam_id}>")
        
        # print(result)
        return result


    # us_06

    def store_divorce_date(self, id):
        the_date = str()
        for family in self.Familis.values():
            if family.fam_ID == id:
                if family.div_date == 'NA':
                    return None
                else:
                    the_date = family.div_date
                    break
        else:
            raise ValueError("Check Family ID")

        return the_date

    def store_death_date(self, id):
        the_date = str()
        for people in self.People.values():
            if people._id == id:
                if people._dday == 'N/A':
                    return None
                else:
                    the_date = people._dday
                    break
        else:
            raise ValueError("Check Individual ID")

        return the_date

    def us_06_compare_divrdate_ddate(self, fam_ID, ind_ID_1, ind_ID_2):
        try:
            fam_date = self.store_divorce_date(fam_ID)
            ind_date_1 = self.store_death_date(ind_ID_1)
            ind_date_2 = self.store_death_date(ind_ID_2)
        except ValueError as e:
            if e == "Check Individual ID":
                # print("ERROR: INDIVIDUAL: us06: Individual not exist")
                raise ValueError("ERROR: INDIVIDUAL: us06: Individual not exist")
            if e == "Check Family ID":
                # print("ERROR: FAMILY: us06: Family not exist")
                raise ValueError("ERROR: INDIVIDUAL: us06: Individual not exist")
        else:
            if (fam_date is None):
                # print("ANOMALY: FAMILY: us06: {fam_ID} divorce data not exist".format(fam_ID=fam_ID))
                raise ValueError("ANOMALY: FAMILY: us06: {fam_ID} divorce data not exist".format(fam_ID=fam_ID))
            elif (ind_date_1 is None) or (ind_date_2 is None):
                # print("ANOMALY: FAMILY: us06: {ind_ID_1} or {ind_ID_2} death date not exist".format(ind_ID_1=ind_ID_1, ind_ID_2=ind_ID_2))
                raise ValueError("ANOMALY: FAMILY: us06: {ind_ID_1} or {ind_ID_2} death date not exist".format(ind_ID_1=ind_ID_1, ind_ID_2=ind_ID_2))
            else:
                return True

    # us_07
    def us07_age_less_150(self):
        # result = ''

        # bdt = datetime.datetime.strptime(self.People[individual_ID]._bday, '%d %b %y')
        result_list = []
        for people in self.People.values():
            if people._age > 150:
                print(f"ERROR: US07: Individual{people._id}> age is > 150 years old")
                result_list.append(f"ERROR: US07: Individual{people._id}> age is > 150 years old")
        else:
            print(f"ANOMALY: US07: Individual{people._id}> didn't record age")
            result_list.append(f"ANOMALY: US07: Individual{people._id}> didn't record age")
        return result_list

    # us_08

    def find_parents_mdate(self, indi_id):
        ''' find individual married date by id in family tree'''

        for i in self.People.values():
            if indi_id == i._id:
                try:
                    self.Familis[i._child]
                except KeyError:  # N/A didn't record parents
                    return "Can't find!"
                else:
                    # NA didn't record married date
                    return self.Familis[i._child].mar_date if self.Familis[i._child].mar_date != "NA" else None

    def find_parents_divdate(self, indi_id):
        ''' find individual divoice date by id in family tree'''

        for i in self.People.values():
            if indi_id == i._id:
                try:
                    self.Familis[i._child]
                except KeyError:  # N/A didn't record parents
                    return "Can't find!"
                else:
                    # NA didn't record div date
                    return self.Familis[i._child].div_date if self.Familis[i._child].div_date != "NA" else None

    def us08_birth_b4_parents_marriage(self):
        '''Children should be born after marriage of parents (and not more than 9 months after their divorce)'''
        result_list = []

        for indi_id in self.People:
            birth_date = self.find_indi_bdate(indi_id)
            married_date = self.find_parents_mdate(indi_id)
            divoce_date = self.find_parents_divdate(indi_id)

            birth_date = datetime.datetime.strptime(birth_date, "%d %b %Y")
            if divoce_date == "Can't find!" or married_date == "Can't find!" or married_date is None:
                print(f"ANOMALY: US08: Individual{indi_id}> Can't compare marriage date and divorce date")
                result_list.append(f"ANOMALY: US08: Individual{indi_id}> Can't compare marriage date and divorce date")
            else:
                married_date = datetime.datetime.strptime(married_date, "%Y-%m-%d")
                if birth_date < married_date:
                    print(f"ERROR: US08: Individual{indi_id}> Birth date is before Marriage")
                    result_list.append(f"ERROR: US08: Individual{indi_id}> Birth date is before Marriage")
                if divoce_date:
                    last_date = datetime.datetime.strptime(divoce_date, "%Y-%m-%d") + datetime.timedelta(days=+270)
                    if last_date <= birth_date:
                        print(f"ERROR: US08: Individual{indi_id}> Birth date is before Marriage")
                        result_list.append(f"ERROR: US08: Individual{indi_id}> Birth date is before Marriage")

        return result_list

    # us_09
    def find_mother_id(self, ind_id):

        for i in self.People.values():
            if ind_id == i._id:
                try:
                    self.Familis[i._child]
                except KeyError:  # N/A didn't record parents
                    return "Can't find!"
                else:
                    # 1)NA didn't record married date 2) I think wife_id(indi's mother) have to exist
                    # if self.Familis[i._child].wife_id != "NA" else None
                    return self.Familis[i._child].wife_id

    def find_father_id(self, ind_id):

        for i in self.People.values():
            if ind_id == i._id:
                try:
                    self.Familis[i._child]
                except KeyError:  # N/A didn't record parents
                    return "Can't find!"
                else:
                    # 1)NA didn't record married date 2) I think wife_id(indi's mother) have to exist
                    # if self.Familis[i._child].hus_id != "NA" else None
                    return self.Familis[i._child].hus_id

    # us3 defined the function below
    '''def find_indi_ddate(self, indi_id):
        """ find individual death date by id in family tree"""
        for i in self.People.values():

            if indi_id == i._id:
                if i._dday != 'N/A':
                    return i._dday
                else:
                    return None
                #return i._dday if i._dday != "N/A" else None
        else:
            raise ValueError'''

    def us09_birth_b4_parents_death(self):
        '''Child should be born before death of mother and before 9 months after death of father'''
        result_list = []
        
        for ind_id in self.People:

            birth_date = self.find_indi_bdate(ind_id)
            mother_id = self.find_mother_id(ind_id)
            mother_ddate = self.find_indi_ddate(mother_id)
            father_id = self.find_father_id(ind_id)
            father_ddate = self.find_indi_ddate(father_id)
            
            try:
                datetime.datetime.strptime(father_ddate, "%d %b %Y")
                mother_ddate_dt = datetime.datetime.strptime(mother_ddate, "%d %b %Y")
                birth_date_dt = datetime.datetime.strptime(birth_date, "%d %b %Y")
            except TypeError:
                print(f"ANOMALY: US09: Individual{ind_id}> Can't compare birth date and parents' death date")
                result_list.append(f"ANOMALY: US09: Individual{ind_id}> Can't compare birth date and parents' death date")

            else:
                last_date = datetime.datetime.strptime(father_ddate, "%d %b %Y") + datetime.timedelta(days=+270)
                if birth_date_dt > last_date or birth_date_dt > mother_ddate_dt:
                
                    print(f"ERROR: US09: Individual{ind_id}> Birth date is after parents' death date")
                    result_list.append(f"ERROR: US09: Individual{ind_id}> Birth date is after parents' death date")
        return result_list

    # us_10

    def us10_marriage_after_14(self):
        """Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old)"""
        result_list = []
        for fam_id in self.Familis:
            if self.Familis[fam_id].mar_date != 'NA':
                mdt = datetime.datetime.strptime(self.Familis[fam_id].mar_date, '%Y-%m-%d')
                hus_id = self.Familis[fam_id].hus_id
                wife_id = self.Familis[fam_id].wife_id
                hbdt = datetime.datetime.strptime(
                    self.People[hus_id]._bday, '%d %b %Y')
                wbdt = datetime.datetime.strptime(
                    self.People[wife_id]._bday, '%d %b %Y')
                hmage = mdt.year-hbdt.year - \
                    ((mdt.month, mdt.day) < (hbdt.month, hbdt.day))
                wmage = mdt.year-wbdt.year - \
                    ((mdt.month, mdt.day) < (wbdt.month, wbdt.day))
                if hmage < 14 or wmage < 14:
                    print(f"ERROR: US10: Family{fam_id}> parents are not at least 14 years old")
                    result_list.append(f"ERROR: US10: Family{fam_id}> parents are not at least 14 years old")
            else:
                print(f"ANOMALY: US10: Family{fam_id}> can't compare if parents are at least 14 years old")
                result_list.append(f"ANOMALY: US10: Family{fam_id}> can't compare if parents are at least 14 years old")
        return result_list

# us_12
    def us12_parents_not_2_old(self):
        """
            Fixed a bug that in for loop, it should read values instead of key-value pairs.
            Fixed a bug that the difference between father's age and child(ren)'s age should be less than 80 instead of 60
        """
        for fam in self.Familis.values():
            if fam.wife_id != 'NA':
                wife = self.getPeople(fam.wife_id)
                if wife._age == "N/A":
                    raise TypeError("ERROR: INDIVIDUAL: us12: Wife age does not exist. ")
            else:
                wife = None
            if fam.hus_id != 'NA':
                hus = self.getPeople(fam.hus_id)
                if hus._age == "N/A":
                    raise TypeError("ERROR: INDIVIDUAL: us12: Husband age does not exist. ")
            else:
                hus = None
            if fam.child_id != ['NA']:
                childs = list()
                for child in fam.child_id:
                    childs.append(self.getPeople(child))
            else:
                print("ANORMALY: FAMILY: us12: {id} has no children".format(id=fam.fam_ID))
                continue
            for child in childs:
                if child._age == "N/A":
                    raise TypeError("ERROR: INDIVIDUAL: us12: Child {id} age does not exist.".format(id=child._id))

            for child in childs:
                if wife is None or hus is None:
                    raise ValueError("ERROR: INDIVIDUAL: us12: Child {id} has not parents".format(id=child._id))
                if ((wife._age - child._age) > 60):
                    raise TypeError("ANORMALY: INDIVIDUAL: us12: Mother is too young or child {id} is too old!".format(id=child._id))
                if ((hus._age - child._age) > 80):
                    raise TypeError("ANORMALY: INDIVIDUAL: us12: Father is too young or child {id} is too old!".format(id=child._id))
        return True

    # us_14
    def us14_multiple_birth_less_5(self):
        """Given a fam_id, check for all child's birthday within the family, no more than 5 siblings should be born at the same time"""
        result = []
        for fam_id, fam in self.Familis.items():

            if len(fam.child_id) >= 5:  # Check for family with more than 5 children

                dd = defaultdict(int)
                for i in fam.child_id:  # Initiate the defaultdict if there is nothing in dd.keys()
                    if dd.keys() == []:
                        dd[self.People[i]._bday] += 1
                    else:
                        for date in dd.keys():  # If there is something in dd,keys(), compare the birthday of new child_id with all existing key in dd.keys()
                            dt1 = datetime.datetime.strptime(
                                self.People[i]._bday, '%d %b %Y')
                            dt2 = datetime.datetime.strptime(date, '%d %b %Y')
                            # How many dates in between birthday of new child_id and one existing key in dd
                            days = abs(dt1 - dt2).days
                            if 0 <= days <= 1:  # If within one date, add to existing key
                                dd[date] += 1
                                break

                        else:
                            # If more than one date, count as new key.
                            dd[self.People[i]._bday] += 1

                for num in dd.values():
                    if num >= 5:
                        print(f"Error: FAMILY<{fam_id}>, US14: Multiple birth more than 5!")
                        result.append(f"Error: FAMILY<{fam_id}>")
    
        # print(result)
        return result

    # us_11

    def US11_No_Bigamy(self):
        ''' For a given ind_id, check if the individual has more than 1 spounse during each marriage'''
        result_list = []

        family_list = list(self.Familis.values())
        i = 1
        for fam_1 in family_list:
            for fam_2 in family_list[i:]:
                if fam_1.fam_ID != fam_2.fam_ID:
                    if fam_1.hus_id == fam_2.hus_id or fam_1.wife_id == fam_2.wife_id:
                        if fam_1.div_date == 'NA' and fam_2.div_date == 'NA':
                            print(f"Error: US11: FAMILY<{fam_1.fam_ID}> husband {fam_1.hus_id} has more than 1 spounse during marriage in family {fam_2.fam_ID}!")
                            result_list.append(f"Error: US11: FAMILY<{fam_1.fam_ID}> husband {fam_1.hus_id} has more than 1 spounse during marriage in family {fam_2.fam_ID}!")

                        elif fam_1.mar_date < fam_2.mar_date and fam_1.div_date > fam_2.mar_date:
                            print(f"Error: US11: FAMILY<{fam_1.fam_ID}> husband {fam_1.hus_id} has more than 1 spounse during marriage in family {fam_2.fam_ID}!")
                            result_list.append(f"Error: US11: FAMILY<{fam_1.fam_ID}> husband {fam_1.hus_id} has more than 1 spounse during marriage in family {fam_2.fam_ID}!")

                i += 1
        return result_list

    # us_15
    def US15_Fewer_15_Child(self):
        '''For a given fam_id, check if the family has more than 15 children'''
        result_list = []

        for family in self.Familis.values():
            if len(family.child_id) >= 15:
                print(f"Error: US15: FAMILY<{family.fam_ID}> has more than 15 children!")
                result_list.append(f"Error: US15: FAMILY<{family.fam_ID}> has more than 15 children!")
        return result_list

    # us_16

    def us16_male_last_names(self):
        """Check within a family to see if husband's lastname matches with child's lastname"""
        result = []
        for fam in self.Familis.values():
            hus_lastname = ''
            child_lastname = []
            if fam.hus_id != 'NA' and fam.child_id != ['NA']:
                hus_lastname = (self.People[fam.hus_id]._name).rstrip(
                    '/').split('/').pop()
                for i in fam.child_id:
                    child_lastname.append(
                        (self.People[i]._name).rstrip('/').split('/').pop())

                for i in child_lastname:
                    if i != hus_lastname:
                        print(f"Error: FAMILY:<{fam.fam_ID}>, US16: Last names don't match")
                        result.append(f"Error: FAMILY:<{fam.fam_ID}>")

        # print(result)
        return result

    # us_13

    def us13_sibling_spacing(self, fam_id):
        '''Birth dates of siblings should be more than 8 months apart or less than 2 days apart (twins may be born one day apart'''
        child_lst = list()
        for fam in self.Familis.values():
            if fam.fam_ID == fam_id:
                for id in fam.child_id:
                    child_lst.append(self.getPeople(id))
                break
        else:
            raise KeyError("ERROR: FAMILY: us13: {fam_id} not exist".format(fam_id=fam_id))
        
        if len(child_lst) <= 1:
            """
            No siblings
            """
            return True
        else:
            for child_1 in child_lst:
                for child_2 in child_lst:
                    if (child_1._id != child_2._id):
                        """
                            It cannot be the same person
                        """
                        if ((datetime.datetime.strptime(child_1._bday, '%d %b %Y') - datetime.datetime.strptime(child_2._bday, '%d %b %Y')).days > 2) or ((datetime.datetime.strptime(child_1._bday, '%d %b %Y') - datetime.datetime.strptime(child_2._bday, '%d %b %Y')).days < 240):
                            raise TypeError("ANORMALY: INDIVIDUAL: us13: Wrong birthday between siblings {child_id_1}, {child_id_2}".format(child_id_1=child_1._id, child_id_2=child_2._id))
            return True
    
    # us_21 Correct gender for role
    def us21_correct_gender(self):
        '''Husband in family should be male and wife in family should be female'''
        result_list = []
        for fam in self.Familis.values():
            if fam.hus_id != "NA" and fam.wife_id != "NA":
                if self.People[fam.hus_id]._gender != "M" or self.People[fam.wife_id]._gender != "F":
                    print(f"ERROR: US21: FAMILY:<{fam.fam_ID}> The role is incorrect")
                    result_list.append(f"ERROR: US21: FAMILY:<{fam.fam_ID}> The role is incorrect")
            else:
                print(f"ANOMALY: US21: Family{fam.fam_ID}> can't compare if the roles of parents are correct")
                result_list.append(f"ANOMALY: US21: Family{fam.fam_ID}> can't compare if the roles of parents are correct")
        return result_list

    # us_22 Unique IDs
    def us22_unique_fam_IDs(self):
        '''All family IDs should be unique'''
        count_fam_id = []
        result_list = []
        for fam in self.Familis.values():
            count_fam_id.append(fam.fam_ID)
            if len(count_fam_id) != len(set(count_fam_id)):
                print(f"ERROR: US22: FAMILY:<{fam.fam_ID}> is not unique")
                result_list.append(f"ERROR: US22: FAMILY:<{fam.fam_ID}> is not unique")
        return result_list



    def us22_unique_indi_IDs(self):
        '''All individual IDs should be unique'''
        count_indi_id = []
        result_list = []

        for indi_1 in self.People.values():
            count_indi_id.append(indi_1._id)
            if len(count_indi_id) != len(set(count_indi_id)):
                print(f"ERROR: US22: INDIVIDUAL:<{indi_1._id}> is not unique")
                result_list.append(f"ERROR: US22: INDIVIDUAL:<{indi_1._id}> is not unique")
        return result_list



    # us17 No marriages to children
    def us17_No_marriages_to_children(self):
        '''Parents should not marry any of their children'''
        family_list = list(self.Familis.values())
        result_list = []
        for fam_1 in family_list:
            if fam_1.hus_id != "NA" and fam_1.wife_id != "NA":
                for fam_2 in family_list:
                
                    if fam_1.hus_id in fam_2.child_id and fam_1.wife_id == fam_2.wife_id:
                        print(
                            f"ERROR: US17: FAMILY {fam_2.fam_ID} mother {fam_2.wife_id}> marriages to children {fam_1.hus_id}")
                        result_list.append(
                            f"ERROR: US17: FAMILY {fam_2.fam_ID} mother {fam_2.wife_id}> marriages to children {fam_1.hus_id}")

                    elif fam_1.wife_id in fam_2.child_id and fam_1.hus_id == fam_2.hus_id:
                        print(f"ERROR: US17: FAMILY {fam_2.fam_ID} father {fam_2.hus_id}> marriages to children {fam_1.wife_id}")
                        result_list.append(f"ERROR: US17: FAMILY {fam_2.fam_ID} father {fam_2.hus_id}> marriages to children {fam_1.wife_id}")
        return result_list

    # us18 Siblings should not marry

    def us18_Siblings_should_not_marry(self):
        '''Siblings should not marry one another'''
        family_list = list(self.Familis.values())
        result_list = []

        for fam_1 in family_list:
            for fam_2 in family_list:
                # family can't only have child ID with parents' ID "NA"
                if fam_1.hus_id in fam_2.child_id and fam_1.wife_id in fam_2.child_id:
                    print(f"ERROR: US18: FAMILY {fam_2.fam_ID} marriages")
                    result_list.append(f"ERROR: US18: FAMILY {fam_2.fam_ID} marriages")
        return result_list

    # us_19
    def us_19_cousins_not_marry(self, child_id):
        if child_id not in self.People.keys():
            raise ValueError("ERROR: INDIVIDUAL: us19: Cannot find {id} in this GED file.".format(id=child_id))
        child = self.People[child_id]
        gender = child._gender
        fam_id = self.People[child_id]._child
        if fam_id == 'N/A':
            return "ANORMALY: INDIVIDUAL: us19: {id} does not have family. Poor guy. ".format(id=child_id)
        fam = self.Familis[fam_id]
        try:
            fam_child = self.Familis[self.People[child_id]._spouse]
        except KeyError:
            raise KeyError("ANORMALY: INDIVIDUAL: us19: {id} is a single dog.".format(id=child_id))
        if child._spouse == 'N/A':
            return True
        else:
            if gender == 'F':
                if fam_child.hus_id in fam.child_id:
                    return "ERROR: INDIVIDUAL: us19: {id} marries his cousins".format(id=child_id)
            if gender == 'M':
                if fam_child.wife_id in fam.child_id:
                    return "ERROR: INDIVIDUAL: us19: {id} marries his cousins".format(id=child_id)
        return True

    # us_20
    def us20_aunts_uncle(self, child_id):
        if child_id not in self.People.keys():
            raise ValueError("ERROR: INDIVIDUAL: us20: Cannot find {id} in this GED file".format(id=child_id))
        child = self.People[child_id]
        gender = child._gender
        fam_id = self.People[child_id]._child
        if fam_id == 'N/A':
            return "ANORMALY: INDIVIDUAL: us20: {id} does not have family".format(id=child_id)
        fam = self.Familis[fam_id]
        father_id = fam.hus_id
        mother_id = fam.wife_id
        if mother_id == 'N/A':
            return "ANORMALY: INDIVIDUAL: us20: {id} does not have mom".format(id=child_id)
        if father_id == 'N/A':
            return "ANORMALY: INDIVIDUAL: us20: {id} does not have dad".format(id=child_id)
        mom = self.People[mother_id]
        dad = self.People[father_id]
        try:
            fam_mom = self.Familis[mom._child]
        except KeyError:
            raise KeyError("ANORMALY: INDIVIDUAL: us20: {mom} parents information not exists".format(mom=mother_id))
        try:
            fam_dad = self.Familis[dad._child]
        except KeyError:
            raise KeyError("ANORMALY: INDIVIDUAL: us20: {dad} parents information not exists".format(dad=father_id))
        if (len(fam_mom.child_id) == 1) and (len(fam_dad.child_id) == 1):
            return "ANORMALY: INDIVIDUAL: us_20: {id} has no uncle or anuts".format(id=child_id)
        if child._spouse == 'N/A':
            return True
        else:
            child_fam = self.Familis[child._spouse]
            if gender == 'F':
                if child_fam.hus_id in fam_mom.child_id:
                    return "ERROR: INDIVIDUAL: us_20: {id} marries aunt or uncle".format(id=child_id)
                if child_fam.hus_id in fam_dad.child_id:
                    return "ERROR: INDIVIDUAL: us_20: {id} marries aunt or uncle".format(id=child_id)
            if gender == 'M':
                if child_fam.wife_id in fam_mom.child_id:
                    return "ERROR: INDIVIDUAL: us_20: {id} marries aunt or uncle".format(id=child_id)
                if child_fam.wife_id in fam_dad.child_id:
                    return "ERROR: INDIVIDUAL: us_20: {id} marries aunt or uncle".format(id=child_id)
            return True

    #us_23
    def us23_unique_name_and_birthday(self):
        """Go through instances of individuals and check for same names and birthdays"""
        result = []
        for ind_id, individule in self.People.items():
            same_name = []
            same_bday = []
            for i in self.People.keys():
                if self.People[i]._name == individule._name:
                    same_name.append(i)
            
            if len(same_name) > 1:
                for j in same_name:
                    if self.People[j]._bday == individule._bday:
                        same_bday.append(j)
                if len(same_bday) == 1:
                    print(f"ANOMALY: INDIVIDULE:<{ind_id}>, US23: Name:<{individule._name}>, <{len(same_name)}> duplicate names were found; No duplicate birthday were found")
                    result.append(f"ANOMALY: INDIVIDULE:<{ind_id}>")
                else:
                    print(f"ERROR: INDIVIDULE:<{ind_id}>, US23: Name:<{individule._name}>, ERROR: Found individule with same name and birthday!")
                    result.append(f"ERROR: INDIVIDULE:<{ind_id}>")

        # print(result)
        return result

    #us_24
    def us24_unique_family_by_spouse(self):
        """Go through instances of Families and check for same spouses' names and marriage dates"""
        result = set()
        for fam_id, fam in self.Familis.items():
            if fam.mar_date != 'NA':
                count = 0
                mdt = {}
                for i in self.Familis.values():
                    if i.mar_date != 'NA':
                        if i.fam_ID != fam.fam_ID:
                            if self.People[i.hus_id]._name == self.People[fam.hus_id]._name and self.People[i.wife_id]._name == self.People[fam.wife_id]._name:
                                mdt[i.fam_ID] = i.mar_date

                if mdt:
                    for fam_id, date in mdt.items():
                        if date == fam.mar_date:
                            result.add(fam_id)
        
        for i in result:
            print(f"ERROR: FAMILY:<{i}>, US24: Families with same spouses and same marriage!")
        # print(result)
        return result
                    

def main():
    path = input("Input path: ")
    filename = input("Input filename: ")
    rep = Repository(filename = filename, dir_path = path)
    #docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    #rep = Repository(filename = r"what_a_mass.ged", dir_path = os.path.join(docs_dir, 'docs'))
    

    #filename = r"Project_t03.ged"
    rep.individual_pt()
    rep.output_family()
    for s in rep.us_01_birth_b4_now():
        if isinstance(s, str):
            print(s)
    rep.us02_birth_b4_marriage()
    rep.us03_birth_b4_death()
    rep.us04_marriage_b4_divoce()
    rep.us05_marriage_b4_death()
    rep.us07_age_less_150()
    rep.us08_birth_b4_parents_marriage()
    rep.us09_birth_b4_parents_death()
    rep.us10_marriage_after_14()
    rep.US11_No_Bigamy()
    rep.us14_multiple_birth_less_5()
    rep.US15_Fewer_15_Child()
    rep.us16_male_last_names()
    rep.us17_No_marriages_to_children()
    rep.us18_Siblings_should_not_marry()

    #rep.us_19_cousins_not_marry()
    for people_id in rep.People.keys():
        try:
            s = rep.us_19_cousins_not_marry(people_id)
            if s is not True:
                print(s)
        except ValueError as e:
            print(e)
        except KeyError as ke:
            print(ke)

    #rep.us20_aunts_uncle()
    for people_id in rep.People.keys():
        try:
            s = rep.us20_aunts_uncle(people_id)
            if s is not True:
                print(s)
        except KeyError as ke:
            print(ke)
        except ValueError as e:
            print(e)

    rep.us21_correct_gender()
    rep.us22_unique_fam_IDs()
    rep.us23_unique_name_and_birthday()
    rep.us24_unique_family_by_spouse()

    for fam_id in rep.Familis.keys():
        try:
            rep.us13_sibling_spacing(fam_id)
        except KeyError as ke:
            print(ke)
        except TypeError as te:
            print(te)
        try:
            rep.us_06_compare_divrdate_ddate(fam_id, "@I10@", "@I11@")
        except ValueError as e:
            print(e)


    try:
        rep.us12_parents_not_2_old()
    except TypeError as te:
        print(te)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
    
