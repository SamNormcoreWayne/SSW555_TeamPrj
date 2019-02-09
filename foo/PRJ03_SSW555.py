class Family():
    __slots__ = {}

    def __init__(self, fam_ID, married, divorced, hus, wife, child_id):
        self.fam_ID = fam_ID
        self.mar_date = married
        self.div_date = divorced
        self.hus = hus
        self.wife = wife
        self.child_id = child_id
