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

        # print(table.get_string(sortby='ID'))
        return table.get_string(sortby='ID')

    #us_01
    def us_01_birth_b4_now(self):
        for person in self.People.values():
            yield datetime.datetime.strptime(person._bday, '%d %b %Y')

    #us_02
    def us02_birth_b4_marriage(self, fam_id):
        """For a givenn fam_id, check the family marriage date and birthday for each individual, retuen the result"""
        result = ''

        if self.Familis[fam_id].mar_date == 'NA':
            result = 'No marriage date'

        else:
            mdt = datetime.datetime.strptime(self.Familis[fam_id].mar_date, '%Y-%m-%d')
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

    #us_04
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
            if mar_dt > div_dt: #Check if marriage date comes after divoce date
                result = "Err: Divoce before Marriage"
            else:
                result = "Good"

        return f"ID: {fam_id}, Result: {result}"

    #us_05
    def us05_marriage_b4_death(self, fam_id):
        """For a given fam_id, check the family marriage date and death date for each individual belongs to this family, return the result of checking"""
        result = ''
        
        if self.Familis[fam_id].mar_date == 'NA':   #check for marriage date, if there is not marriage date, change result
            result = 'No marriage date'
        
        else:
            mdt = datetime.datetime.strptime(self.Familis[fam_id].mar_date, '%Y-%m-%d') #If there is marriage date, covert it to datetime object
            ddates = []
            hus_id = self.Familis[fam_id].hus_id
            wife_id = self.Familis[fam_id].wife_id
            ddates.append(self.People[hus_id]._dday)    #Get husband's death date in ddate, coule be 'N/A'
            ddates.append(self.People[wife_id]._dday)   #Get wife's death date in ddate, could be 'N/A'
            for i in ddates:
                if i != 'N/A':  #Check elements in ddate, if there is a death date, compare it with marriage date(mdt), if death date was before marriage date, change reuslt and break out of loop
                    ddt = datetime.datetime.strptime(i, '%d %b %Y')
                    if ddt < mdt:
                        result = "Error: Death before marriage"
                        break
            
            else:
                result = 'Good' #If both elements are 'N/A' or after marriage date, change result to 'Good'

        
        return f"Family ID: {fam_id}, Result: {result}"

    #us_06
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

    #us_07
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
    
    #us_10
    def us10_marriage_after_14(self, fam_id):
        """For a given fam_id, check the family marriage date and death date for each individual belongs to this family, return the result of checking"""
        
        result='No Marriage date'

        if self.Familis[fam_id].mar_date != 'NA':   #check for marriage date, if there is not marriage date, change result
            mdt = datetime.datetime.strptime(self.Familis[fam_id].mar_date, '%Y-%m-%d') #If there is marriage date, covert it to datetime object
            hus_id = self.Familis[fam_id].hus_id
            wife_id = self.Familis[fam_id].wife_id
            hbdt = datetime.datetime.strptime(self.People[hus_id]._bday, '%d %b %Y')
            wbdt = datetime.datetime.strptime(self.People[wife_id]._bday, '%d %b %Y')
            hmage = mdt.year-hbdt.year-((mdt.month, mdt.day) < (hbdt.month, hbdt.day))
            wmage= mdt.year-wbdt.year-((mdt.month, mdt.day) < (wbdt.month, wbdt.day))
            if hmage<14 or wmage < 14:
                    result = 'ERROR'
            else:
                result = 'Good'
        return f"ID: {fam_id}, Result: {result}"

    def us12_parents_not_2_old(self):
        for fam in self.Familis:
            if fam.wife_id != 'N/A':
                wife = self.getPeople(fam.wife_id)
            if fam.hus_id != 'N/A':
                hus = self.getPeople(fam.hus_id)
            if fam.child_id != ['N/A']:
                childs = list()
                for child in fam.child_id:
                    childs.append(self.getPeople(child))

        if wife._age == "N/A":
            raise TypeError("Wife age does not exist. ")
        if hus._age == "N/A":
            raise TypeError("Husband age does not exist. ")

        for child in childs:
            if child._age == "N/A":
                raise TypeError("Child {id} age does not exist.".format(id=child._id))

        for child in childs:
            if (wife._age - child._age) < 60:
                raise TypeError("Mother is too young or child {id} is too old!".format(id=child._id))
            else:
                return True
            if (hus._age - child._age) < 60:
                raise TypeError("Father is too young or child {id} is too old!".format(id=child._id))
            else:
                return True


def main():
    path = input("Input path: ")
    filename = input("Input filename: ")
    rep = Repository(filename=filename, dir_path=path)
    print(rep.individual_pt())
    print(rep.output_family())


if __name__ == "__main__":
    main()
