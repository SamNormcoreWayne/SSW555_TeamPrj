import os
import datetime
from CheckGED import get_fam, get_indi
from prettytable import PrettyTable


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
        self._child = ''
        self._spouse = ''

    def add_name(self, name):
        """Add person's name to instance"""
        self._name = name

    def add_sex(self, sex):
        """Add gender information to instance"""
        self._gender = sex

    def add_bday(self, bday):
        """Add birthday to instace"""
        self._bday = bday
        dt1 = datetime.datetime.strptime(bday, '%d %b %Y')
        dt2 = datetime.datetime.now()
        self._age = ((dt2 - dt1).days) // 365

    def add_dday(self, dday):
        """Add death infotmation to istance is needed"""
        self._alive = False
        self._dday = dday

    def pt_row(self):
        """Return information needed for prettytable"""
        return self._id, self._name, self._gender, self._bday, self._age, self._alive, self._dday, self._child, self._spouse

    def add_child(self):
        None

    def add_spouse(self):
        None

    def __str__(self):
        """Convert info to string"""
        return f"Individule:{self._id}, name: {self._name}, gender:{self._gender}, bday: {self._bday}, alive: {self._alive}, dday: {self._dday}, age: {self._age}"


class Family():
    __slots__ = {}

    def __init__(self, fam_ID, married, divorced, hus, wife, child_id):
        self.fam_ID = fam_ID
        self.mar_date = married
        self.div_date = divorced
        self.hus = hus
        self.wife = wife
        self.child_id = child_id


class Repository():
    def __init__(self, filename, dir_path=os.getcwd()):
        self.People = dict()
        self.Familis = dict()
        self.working_path = dir_path
        self.read_indi(dir_path, filename)
        self.read_detail(dir_path, filename)

    def read_indi(self, path, filename):
        """Read through file, combine information for each person and create a istance of Individual"""
        dd = get_indi(path, filename)
        for i in dd.keys():
            self.People[i] = Individual(i)

    def read_detail(self, path, filename):
        """Read all detail information for each person, and modify the instaces accordigly"""
        dd = get_indi(path, filename)
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

    def individual_pt(self):
        """Create prettytable for all instances of class Individual"""
        pt = PrettyTable(field_names=Individual.pt_labels)
        for individual in self.People.values():
            pt.add_row(individual.pt_row())

        print(pt, '\n')

    def input_family(self):
        path = self.working_path
        filename = self.filename
        child_ids = list()
        fam_lst = list(get_fam(path, filename))
        for fam_dic in fam_lst:
            hus = self.getPeople(fam_dic['hus_name'])
            wife = self.getPeople(fam_dic['wife_name'])
            for child_name in fam_dic['child_names']:
                child_ids.append(self.getPeople_id(child_name))
            new_family = Family(fam_dic['fam_ID'], fam_dic['mar_date'], fam_dic['div_date'], hus, wife, child_ids)
            self.Familis.append(new_family)

    def getPeople(self, name):
        for individual in self.People.values():
            if individual.name == name:
                return individual

    def getPeople_id(self, name):
        for individual in self.People.values():
            if name == individual.name:
                return individual.ID

    def output_family(self):
        field_name = ['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children']
        table = PrettyTable(field_names=field_name)
        for family in self.Familis:
            table.add_row([family.fam_ID, family.mar_date, family.div_date, family.hus.ID, family.hus.name, family.wife.ID, family.wife.name, family.child_ids])

        print(table.get_string())
