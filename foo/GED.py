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

        print(table.get_string(sortby='ID'))
        return table.get_string(sortby='ID')

    # us_01
    def us_01_birth_b4_now(self):
        for person in self.People.values():
            yield datetime.datetime.strptime(person._bday, '%d %b %Y')

    # us_02
    def us02_birth_b4_marriage(self, fam_id):
        """For a givenn fam_id, check the family marriage date and birthday for each individual, retuen the result"""
        result = ''

        if self.Familis[fam_id].mar_date == 'NA':
            result = 'No marriage date'

        else:
            mdt = datetime.datetime.strptime(
                self.Familis[fam_id].mar_date, '%Y-%m-%d')
            child_id = self.Familis[fam_id].child_id
            bdates = [self.People[i]._bday for i in child_id]
            for i in bdates:
                if i == 'N/A':
                    raise ValueError("Not birthday found for this person")
                else:
                    bdt = datetime.datetime.strptime(i, '%d %b %Y')
                    if bdt < mdt:
                        result = 'Error: Birth before marriage'
                        break

            else:
                result = 'Good'

        return f"Family ID: {fam_id}, Result: {result}"

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

    # us_04
    def us04_marriage_b4_divoce(self, fam_id):
        """Compare marriage date and divoce date(if available) for each family"""

        #result = ''
        mar_date = self.Familis[fam_id].mar_date
        div_date = self.Familis[fam_id].div_date
        if mar_date == 'NA':
            result = "No marriage date"
        elif div_date == 'NA':
            result = "No divoce date"
        else:
            mar_dt = datetime.datetime.strptime(mar_date, "%Y-%m-%d")
            div_dt = datetime.datetime.strptime(div_date, "%Y-%m-%d")
            if mar_dt > div_dt:  # Check if marriage date comes after divoce date
                result = "Err: Divoce before Marriage"
            else:
                result = "Good"

        return f"ID: {fam_id}, Result: {result}"

    # us_05
    def us05_marriage_b4_death(self, fam_id):
        """For a given fam_id, check the family marriage date and death date for each individual belongs to this family, return the result of checking"""
        result = ''

        # check for marriage date, if there is not marriage date, change result
        if self.Familis[fam_id].mar_date == 'NA':
            result = 'No marriage date'

        else:
            # If there is marriage date, covert it to datetime object
            mdt = datetime.datetime.strptime(
                self.Familis[fam_id].mar_date, '%Y-%m-%d')
            ddates = []
            hus_id = self.Familis[fam_id].hus_id
            wife_id = self.Familis[fam_id].wife_id
            # Get husband's death date in ddate, coule be 'N/A'
            ddates.append(self.People[hus_id]._dday)
            # Get wife's death date in ddate, could be 'N/A'
            ddates.append(self.People[wife_id]._dday)
            for i in ddates:
                # Check elements in ddate, if there is a death date, compare it with marriage date(mdt), if death date was before marriage date, change reuslt and break out of loop
                if i != 'N/A':
                    ddt = datetime.datetime.strptime(i, '%d %b %Y')
                    if ddt < mdt:
                        result = "Error: Death before marriage"
                        break

            else:
                result = 'Good'  # If both elements are 'N/A' or after marriage date, change result to 'Good'

        return f"Family ID: {fam_id}, Result: {result}"

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

    def compare_divrdate_ddate(self, fam_ID, ind_ID_1, ind_ID_2):
        try:
            fam_date = self.store_divorce_date(fam_ID)
            ind_date_1 = self.store_death_date(ind_ID_1)
            ind_date_2 = self.store_death_date(ind_ID_2)
        except ValueError:
            raise ValueError("Check Individual ID or Family ID")
        else:
            if (fam_date is None) or (ind_date_1 is None) or (ind_date_2 is None):
                raise ValueError("Birthday or divorce date does not exist")
            else:
                return True

    # us_07
    def us07_age_less_150(self, individual_ID):
        # result = ''

        # bdt = datetime.datetime.strptime(self.People[individual_ID]._bday, '%d %b %y')
        for people in self.People.values():
            if people._id == individual_ID:
                if people._age > 150:
                    raise(ValueError("The age is more than 150"))
                else:
                    return True
        return False

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

    def us08_birth_b4_parents_marriage(self, ind_id):
        '''Children should be born after marriage of parents (and not more than 9 months after their divorce)'''
        try:
            birth_date = self.find_indi_bdate(ind_id)
            married_date = self.find_parents_mdate(ind_id)
            divoce_date = self.find_parents_divdate(ind_id)
        except ValueError:
            return "Can't find!"
        else:
            if divoce_date != "Can't find!" and married_date != "Can't find!":
                last_date = datetime.datetime.strptime(
                    divoce_date, "%Y-%m-%d") + datetime.timedelta(days=+270)
                birth_date = datetime.datetime.strptime(birth_date, "%d %b %Y")
                divoce_date = datetime.datetime.strptime(
                    divoce_date, "%Y-%m-%d")
                married_date = datetime.datetime.strptime(
                    married_date, "%Y-%m-%d")
                if birth_date > married_date and divoce_date is None:
                    return True
                elif birth_date > married_date and last_date >= birth_date:
                    return True
                else:
                    return False
            else:
                return "Can't compare!"

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

    def us09_birth_b4_parents_death(self, ind_id):
        '''Child should be born before death of mother and before 9 months after death of father'''
        birth_date = self.find_indi_bdate(ind_id)
        mother_id = self.find_mother_id(ind_id)
        mother_ddate = self.find_indi_ddate(mother_id)
        father_id = self.find_father_id(ind_id)
        father_ddate = self.find_indi_ddate(father_id)
        try:
            datetime.datetime.strptime(father_ddate, "%d %b %Y")
            mother_ddate_dt = datetime.datetime.strptime(
                mother_ddate, "%d %b %Y")
            birth_date_dt = datetime.datetime.strptime(birth_date, "%d %b %Y")
        except TypeError:
            return "Can't compare"
        else:
            last_date = datetime.datetime.strptime(
                father_ddate, "%d %b %Y") + datetime.timedelta(days=+270)
            if birth_date_dt < last_date and birth_date_dt <= mother_ddate_dt:
                return True
            else:
                return False

    # us_10

    def us10_marriage_after_14(self, fam_id):
        """For a given fam_id, check the family marriage date and death date for each individual belongs to this family, return the result of checking"""

        result = 'No Marriage date'

        # check for marriage date, if there is not marriage date, change result
        if self.Familis[fam_id].mar_date != 'NA':
            # If there is marriage date, covert it to datetime object
            mdt = datetime.datetime.strptime(
                self.Familis[fam_id].mar_date, '%Y-%m-%d')
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
                result = 'ERROR'
            else:
                result = 'Good'
        return f"ID: {fam_id}, Result: {result}"

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
                    raise TypeError("Wife age does not exist. ")
            else:
                wife = None
            if fam.hus_id != 'NA':
                hus = self.getPeople(fam.hus_id)
                if hus._age == "N/A":
                    raise TypeError("Husband age does not exist. ")
            else:
                hus = None
            if fam.child_id != ['NA']:
                childs = list()
                for child in fam.child_id:
                    childs.append(self.getPeople(child))
            else:
                childs = None

            if (childs is not None):
                for child in childs:
                    if child._age == "N/A":
                        raise TypeError(
                            "Child {id} age does not exist.".format(id=child._id))

                for child in childs:
                    if ((wife._age - child._age) > 60) and (wife is not None):
                        raise TypeError(
                            "Mother is too young or child {id} is too old!".format(id=child._id))
                    if ((hus._age - child._age) > 80) and (hus is not None):
                        raise TypeError(
                            "Father is too young or child {id} is too old!".format(id=child._id))
                return True
            return "No Children"

    # us_14
    def us14_multiple_birth_less_5(self, fam_id):
        """Given a fam_id, check for all child's birthday within the family, no more than 5 siblings should be born at the same time"""
        fam = self.Familis[fam_id]
        result = ''

        if len(fam.child_id) < 5:
            result = 'Good'

        else:
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
                    result = 'Error: Multiple birth more than 5'
                    break

            else:
                result = 'Good'

        return f"ID: {fam_id}, Reslut: {result}"

    # us_11
    def US11_No_Bigamy(self):
      # For a given ind_id, check if the individual has more than 1 spounse during each marriage
        for fam_1 in self.Familis.values():
            for fam_2 in self.Familis.values():
                if fam_1.fam_ID != fam_2.fam_ID:
                    if fam_1.hus_id == fam_2.hus_id or fam_1.wife_id == fam_2.wife_id:
                        if fam_1.div_date == 'NA' and fam_2.div_date == 'NA':
                            return 'bigamy'
                        elif fam_1.mar_date < fam_2.mar_date and fam_1.div_date > fam_2.mar_date:
                            return 'bigamy'
        else:
            return True

    # us_15
    def US15_Fewer_15_Child(self):
      # For a given fam_id, check if the family has more than 15 children

        for family in self.Familis.values():
            if len(family.child_id) >= 15:
                flag = False
                break
        else:
            flag = True

        return flag

    # us_16

    def us16_male_last_names(self, fam_id):
        """Check within a family to see if husband's lastname matches with child's lastname"""
        fam = self.Familis[fam_id]
        hus_lastname = ''
        child_lastname = []

        if fam.hus_id == 'NA':
            raise ValueError("Husband not found")
        elif fam.child_id == ['NA']:
            raise ValueError("Child not found")
        else:
            hus_lastname = (self.People[fam.hus_id]._name).rstrip(
                '/').split('/').pop()
            for i in fam.child_id:
                child_lastname.append(
                    (self.People[i]._name).rstrip('/').split('/').pop())

            for i in child_lastname:
                if i != hus_lastname:
                    result = "Error: Last names don't match"
                    break
            else:
                result = "Good"

        print(hus_lastname, child_lastname)

        return f"ID: {fam_id}, Result: {result}"

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
            raise KeyError

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
                        if ((child_1._bday - child_2._bday).days > 2) or ((child_1._bday - child_2._bday).days < 240):
                            raise TypeError("Wrong birthday between siblings")
            return True

    # us17 No marriages to children
    def us17_No_marriages_to_children(self):
        '''Parents should not marry any of their children'''
        family_list = list(self.Familis.values())
        i = 1
        result_list = []
        for fam_1 in family_list:
            for fam_2 in family_list[i:]:
                if fam_1.hus_id != "NA" and fam_1.wife_id != "NA":

                    if fam_1.hus_id in fam_2.child_id and fam_1.wife_id == fam_2.wife_id:
                        print(
                            f"ERROR: US17: FAMILY {fam_1.fam_ID} father {fam_1.hus_id}> marriages to children {fam_2.child_id}")
                        result_list.append(
                            f"ERROR: US17: FAMILY {fam_1.fam_ID} father {fam_1.hus_id}> marriages to children {fam_2.child_id}")

                    elif fam_1.wife_id in fam_2.child_id and fam_1.hus_id == fam_2.hus_id:
                        print(f"ERROR: US17: FAMILY {fam_1.fam_ID} mother {fam_1.wife_id}> marriages to children {fam_2.child_id}")
                        result_list.append(f"ERROR: US17: FAMILY {fam_1.fam_ID} mother {fam_1.wife_id}> marriages to children {fam_2.child_id}")
            i += 1
        return result_list

    # us18 Siblings should not marry

    def us18_Siblings_should_not_marry(self):
        '''Siblings should not marry one another'''
        family_list = list(self.Familis.values())
        i = 1
        result_list = []

        for fam_1 in family_list:
            for fam_2 in family_list[i:]:
                # family can't only have child ID with parents' ID "NA"
                if fam_1.hus_id in fam_2.child_id and fam_1.wife_id in fam_2.child_id:
                    print(f"ERROR: US18: FAMILY {fam_2.fam_ID} marriages")
                    result_list.append(f"ERROR: US18: FAMILY {fam_2.fam_ID} marriages")

            i += 1
        return result_list


def main():
    '''path = input("Input path: ")
    filename = input("Input filename: ")'''
    path = r"D:\sit study\SSW555\PJ"
    filename = r"Project_t17.ged"
    #filename = r"Project01_Pli.ged"
    rep = Repository(filename=filename, dir_path=path)
    rep.individual_pt()
    rep.output_family()
    a = rep.us17_No_marriages_to_children()
    b = rep.us18_Siblings_should_not_marry()
    print(a)
    print(b)


if __name__ == "__main__":
    main()
