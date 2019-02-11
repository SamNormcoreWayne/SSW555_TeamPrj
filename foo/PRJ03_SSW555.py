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
        self.Family = dict()
        self.working_path = dir_path

    def input_fmality():
        path = os.path.getcwd()
        filename = input("Input file name: ")
        for fam_dic in get
        fam_dic = get_fam(path, filename)
        hus_id = get_individual_id(fam_dic)


    def get_individual_id(name):
        for name in People.values().name:
            return ID
