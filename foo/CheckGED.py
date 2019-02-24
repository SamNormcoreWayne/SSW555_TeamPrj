import os
from datetime import datetime
from collections import defaultdict

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
    file_dir = os.path.join(path, filename)
    try:
        fp = open("{}_output.ged".format(file_dir), 'w')
    except FileNotFoundError:
        print("Cannot open")
    for line in ged_reader(path, filename):
        # print("--> " + line)
        fp.write("--> " + line + '\n')
        line_lst = line.split(' ', 2)
        line_str = check_item(line_lst)
        yield line_str
        # print("<-- " + line_str)
        fp.write("<-- " + line_str + '\n')
    fp.close()


def get_fam(path, filename):
    # Output a dictionary of a family withour their IDs.
    gedlst = list(check_input_output(path, filename))
    date_type = str()
    fam_ID = 'NA'
    for index in range(0, len(gedlst)):
        if index == len(gedlst) - 1:
            break
        tmp = gedlst[index]
        # print("line: {}".format(gedlst[index]))
        # returndic = dict()
        if gedlst[index].startswith("0|FAM|Y|"):
                
                mar_date = 'NA'
                div_date = 'NA'
                hus_name = 'NA'
                wife_name = 'NA'
                child_names = 'NA'
                # print("right line: ", gedlst[index])
                tmp = tmp.split('|')
                # print("list: ", tmp)
                fam_ID = tmp.pop()
                # print(fam_ID)
        if gedlst[index].startswith("1|HUSB|Y|"):
            tmp = tmp.split('|')
            hus_name = tmp.pop()
            # print("hus ", hus_name)
        if gedlst[index].startswith("1|WIFE|Y|"):
            tmp = tmp.split('|')
            wife_name = tmp.pop()
            # print("hus ", hus_name)
        if gedlst[index].startswith("1|CHIL|Y|"):
            tmp = tmp.split('|')
            child_names = tmp.pop().split(' ')

        if gedlst[index].startswith("1|MARR|Y"):
            date_type = 'MARR'
            continue
        if gedlst[index].startswith("1|DIV|Y"):
            date_type = 'DIV'
            continue
        if gedlst[index].startswith("2|DATE|Y|"):
            tmp = tmp.split('|')
            if tmp[-1] != '':
                if date_type == 'MARR':
                    mar_date_type = datetime.strptime(tmp.pop(), "%d %b %Y")
                    mar_date = datetime.strftime(mar_date_type, "%Y-%m-%d")
                if date_type == 'DIV':
                    div_date_type = datetime.strptime(tmp.pop(), "%d %b %Y")
                    div_date = datetime.strftime(div_date_type, "%Y-%m-%d")
                    print("div_date: ", div_date)

                date_type = ""
        if fam_ID != 'NA' and gedlst[index + 1].startswith("0|"):
            yield {'fam_ID': fam_ID, 'mar_date': mar_date, 'div_date': div_date, 'hus': hus_name, 'wife': wife_name, 'children': child_names}


"""
if not gedlst[index].startswith("1|DIV|Y"):
                        yield {'fam_ID': fam_ID, 'mar_date': mar_date, 'div_date': div_date, 'hus': hus_name, 'wife': wife_name, 'children': child_names}
                    else:
                        continue

yield {'fam_ID': fam_ID, 'mar_date': mar_date, 'div_date': div_date, 'hus': hus_name, 'wife': wife_name, 'children': child_names}
"""


def get_indi(path, filename):
    """ by Sherman """
    result = list(check_input_output(path, filename))
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
    filename = "Project01_Xiaomeng Xu.ged"
    path = r"C:\Users\64937\OneDrive\Documents\SSW\555\SSW555_TeamPrj\docs"
    print(path)
    # list(check_input_output(path, filename))
    print(list(get_fam(path, filename)))


if __name__ == '__main__':
    main()
