"""SSW555_P3
    Xiaomeng(Sherman) Xu"""

from prettytable import PrettyTable
import os
from collections import defaultdict
from CheckGED import get_indi
import datetime


class Repository:
    """Repository where we store all families and their content individuales"""

    def __init__(self, path, filename):
        """Cache for families and individuals"""
        self._family = dict()
        self._individual = dict()
        self.read_indi(path, filename)
        self.read_detail(path, filename)

    def read_indi(self, path, filename):
        """Read through file, combine information for each person and create a istance of Individual"""
        dd = get_indi(path, filename)
        for i in dd.keys():
            self._individual[i] = Individual(i)

    def read_detail(self, path, filename):
        """Read all detail information for each person, and modify the instaces accordigly"""
        dd = get_indi(path, filename)
        for i in dd.keys():
            for j in range(len(dd[i])):
                if dd[i][j].startswith('1|NAME|'):
                    self._individual[i].add_name(dd[i][j].split('|')[3])

                elif dd[i][j].startswith('1|SEX|'):
                    self._individual[i].add_sex(dd[i][j].split('|')[3])

                elif dd[i][j].startswith('1|BIRT|'):
                    self._individual[i].add_bday(dd[i][j + 1].split('|')[3])

                elif dd[i][j].startswith('1|DEAT|'):
                    self._individual[i].add_dday(dd[i][j + 1].split('|')[3])

    def individual_pt(self):
        """Create prettytable for all instances of class Individual"""
        pt = PrettyTable(field_names=Individual.pt_labels)
        for individual in self._individual.values():
            pt.add_row(individual.pt_row())

        print(pt, '\n')


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

    def __str__(self):
        """Convert info to string"""
        return f"Individule:{self._id}, name: {self._name}, gender:{self._gender}, bday: {self._bday}, alive: {self._alive}, dday: {self._dday}, age: {self._age}"


def main():
    filename = input('Please enter the file name')
    path = input('Please enter the directory')
    # filename = 'Project01_Xiaomeng Xu.ged'
    # path = '/Users/sherman/Desktop/SSW555'
    GED = Repository(path, filename)
    # print(GED._individual['@I5@'])
    # print(GED._individual['@I2@'])
    # print(GED._individual['@I1@'])
    GED.individual_pt()


if __name__ == '__main__':
    main()