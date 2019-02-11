Testing Report
=====
SSS555 Project 3
-----
Update: 2019-2-11 14:37:07

In PRJ03_SSW555.py:
  - Line 98 to 114 in method read_detail(self):
      ```python
      for i in dd.keys():
          for j in range(len(dd[i])):
              if dd[i][j].startswith('1|NAME|'):
                  self.People[i].add_name(dd[i][j].split('|')[3)

              elif dd[i][j].startswith('1|SEX|'):
                  self.People[i].add_sex(dd[i][j].split('|')[3])

              elif dd[i][j].startswith('1|BIRT|'):
                  self.People[i].add_bday(dd[i][j + 1].split('|')[3])

              elif dd[i][j].startswith('1|DEAT|'):
                  self.People[i].add_dday(dd[i][j + 1].split('|')[3])
              elif dd[i][j].startswith('1|FAMC|'):
                  self.People[i].add_child(dd[i][j + 1].split('|')[3])
              elif dd[i][j].startswith('1|FAMS|'):
                  self.People[i].add_spouse(dd[i][j + 1].split('|')[3])
      ```
    - Related GED code line 22 to 25:
      ```
      1 FAMS @F1@
      1 FAMS @F2@
      1 FAMS @F4@
      1 FAMC @F3@
      ```
    Image:


    Analysis:
