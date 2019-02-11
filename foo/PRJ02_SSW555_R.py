import os
# import unittest
from collections import defaultdict


def getline(path):
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        print("Cannot open {}".format(path))
    else:
        with fp:
            for line in fp:
                yield line


def ged_reader(path, filename):
    if path != "":
        path = os.path.join(path, filename)
    else:
        path = filename
    fp = open("{}_output.ged".format(path), 'w')
    result = list()
    for line in getline(path):
        line = line.rstrip('\n')
        # print("--> " + line)
        fp.write("--> " + line + '\n')
        line_lst = line.split(' ', 2)
        line_str = check_item(line_lst)
        result.append(line_str)
        # print("<-- " + line_str)
        fp.write("<-- " + line_str + '\n')
    fp.close()
    return (result)


def check_item(line_lst):
    top_level_1 = {'HEAD', 'TRLR', 'NOTE'}
    top_level_2 = {'INDI', 'FAM'}
    tag_indi = {'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS'}
    tag_fam = {'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'}
    tag_date = {'DATE'}
    tmp = line_lst

    if tmp[0] == '0':
        if tmp[1].isupper() and tmp[1] in top_level_1:
            tmp[1] = "|{}|Y|".format(tmp[1])
            return to_str(tmp)
        if tmp[2].isupper():
            tmp[1], tmp[2] = tmp[2], tmp[1]
            if tmp[1] in top_level_2:
                tmp[1] = "|{}|Y|".format(tmp[1])
            return to_str(tmp)
        tmp[1] = "|{}|N|".format(tmp[1])
        return to_str(tmp)

    if tmp[0] == '1':
        if tmp[1] in tag_indi or tmp[1] in tag_fam:
            tmp[1] = "|{}|Y|".format(tmp[1])
            return to_str(tmp)
        else:
            tmp[1] = "|{}|N|".format(tmp[1])
            return to_str(tmp)

    if tmp[0] == '2':
        if tmp[1] in tag_date:
            tmp[1] = "|{}|Y|".format(tmp[1])
            return to_str(tmp)
        else:
            tmp[1] = "|{}|N|".format(tmp[1])
            return to_str(tmp)

    tmp[1] = "|{}|N|".format(tmp[1])
    return to_str(tmp)


def to_str(lst):
    s = str()
    try:
        s = lst[0] + lst[1] + lst[2]
    except IndexError:
        s = lst[0] + lst[1]
    return s


'''class TestGedReader(unittest.TestCase):
    def test_ged_reader(self):
        cur_dir = os.getcwd()
        test_dir = os.path.join(cur_dir, "test")
        filename = "test_case.ged"
        ged_reader(test_dir, filename)
        fp_1 = open(os.path.join(test_dir, "right_outcome.ged"))
        fp_2 = open(os.path.join(test_dir, "{}_output.ged".format(filename)))
        self.assertEquals(fp_1.readlines(), fp_2.readlines())
        fp_1.close()
        fp_2.close()'''


def get_indi(path, filename):
    result = ged_reader(path, filename)
    dd = defaultdict(list)
    id = 'NONE'
    for i in range(len(result)):
        if result[i].startswith('0|INDI|Y'):
            id = result[i].split('|')[3]

        elif id == "NONE":
            continue

        else:
            dd[id].append(result[i])

    return dd

def main():
    filename = input("Enter filename:")
    path = input("Enter path:")
    print(path)
    #print(ged_reader(path, filename))
    #print (get_indi(path, filename))
    dd = get_indi(path, filename)
    print(dd['@I1@'])
    print(dd['@I2@'])
    print(dd['@I3@'])


















if __name__ == '__main__':
    #unittest.main(exit=False, verbosity=2)
    main()
