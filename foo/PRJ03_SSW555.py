import os
from CheckGED import get_fam


class Individual():
    def __init__(self):
        self.ID
        self.name


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
    def __init__(self, dir_path=os.getcwd()):
        self.People = dict()
        self.Familis = dict()
        self.working_path = dir_path

    def input_fmality(self):
        path = os.path.getcwd()
        filename = input("Input file name: ")
        child_ids = list()
        fam_lst = list(get_fam(path, filename))
        for fam_dic in fam_lst:
            hus = self.get_individual(fam_dic['hus_name'])
            wife = self.get_individual(fam_dic['wife_name'])
            for child_name in fam_dic['child_names']:
                child_ids.append(self.get_individual_id(child_name))
            new_family = Family(fam_dic['fam_ID'], fam_dic['mar_date'], fam_dic['div_date'], hus, wife, child_ids)
            self.Familis.append(new_family)

    def get_individual(self, name):
        for individual in self.People.values():
            if individual.name == name:
                return individual

    def get_individual_id(self, name):
        for individual in self.People.values():
            if name == individual.name:
                return individual.ID

    def out_put