import os
from datetime import datetime


top_level_1 = {'HEAD', 'TRLR', 'NOTE'}
top_level_2 = {'INDI', 'FAM'}
tag_indi = {'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS'}
tag_fam = {'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'}
tag_date = {'DATE'}


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

    for line in getline(path):
        line = line.rstrip('\n')
        yield line


def check_input_output(path, filename):
    # This method is unnecessary for  prj3.
    # fp = open("{}_output.ged".format(path), 'w')
    for line in ged_reader(path, filename):
        # print("--> " + line)
        # fp.write("--> " + line + '\n')
        line_lst = line.split(' ', 2)
        line_str = check_item(line_lst)
        yield line_str
        # print("<-- " + line_str)
        # fp.write("<-- " + line_str + '\n')
    # fp.close()


def get_fam(path, filename):
    # Output a dictionary of a family withour their IDs.
    gedlst = list(check_input_output(path, filename))
    date_type = str()
    mar_date = ''
    div_date = ''
    for line in gedlst:
        tmp = line
        print("line: {}".format(line))
        # returndic = dict()
        if line.startswith("0|FAM|Y|"):
                print("right line: ", line)
                tmp = tmp.split('|')
                print("list: ", tmp)
                fam_ID = tmp.pop()
                print(fam_ID)
                continue
        if line.startswith("1|HUSB|Y|"):
            tmp = tmp.split('|')
            hus_name = tmp.pop()
            print("hus ", hus_name)
            continue
        if line.startswith("1|WIFE|Y|"):
            tmp = tmp.split('|')
            wife_name = tmp.pop()
            print("hus ", hus_name)
            continue
        if line.startswith("1|CHIL|Y|"):
            tmp = tmp.split('|')
            child_names = tmp.pop().split(' ')
            continue

        if line.startswith("1|MARR|Y"):
            date_type = 'MARR'
            continue
        if line.startswith("1|DIV|Y"):
            date_type = 'DIV'
            continue

        if line.startswith("2|DATE|Y|"):
            if date_type == '':
                continue
            tmp = tmp.split('|')
            if tmp[-1] != '':
                if date_type == 'MARR':
                    mar_date_type = datetime.strptime(tmp.pop(), "%d %b %Y")
                    mar_date = datetime.strftime(mar_date_type, "%Y-%m-%d")
                if date_type == 'DIV':
                    div_date_type = datetime.strptime(tmp.pop(), "%d %b %Y")
                    div_date = datetime.strftime(div_date_type, "%Y-%m-%d")
            else:
                if date_type == 'MARR':
                    mar_date = 'NA'
                if date_type == 'DIV':
                    div_date = 'NA'
            if div_date != '':
                yield {'fam_ID': fam_ID, 'mar_date': mar_date, 'div_date': div_date, 'hus_name': hus_name, 'wife_name': wife_name, 'child_names': child_names}


def check_item(line_lst):
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


def main():
    filename = input("Enter filename:")
    path = input("Enter path:")
    print(path)
    # check_input_output(path, filename)
    print(list(get_fam(path, filename)))


if __name__ == '__main__':
    main()
