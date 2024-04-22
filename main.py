from pprint import pprint
import re
import csv


with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

for i in contacts_list:
 if len(i[0]. split()) > 2:
   i[1]=(i[0].split()[1])
   i[2]=(i[0].split()[2])
   i[0]=(i[0].split()[0])
 elif len(i[0].split()) == 2:
   i[1]=(i[0].split()[1])
   i[0]=(i[0].split()[0])
 elif len(i[1].split()) > 1:
   i[2]=(i[1].split()[1])
   i[1]=(i[1].split()[0])

    
i1 = contacts_list[0]
deleted_list = []
for i in sorted(contacts_list[1:len(contacts_list)]):
  if i[0:2] == i1[0:2]:
    for ind in range(1,7):
      if i1[ind]:
        i[ind] = i1[ind]
    deleted_list.append(i1)
  i1 = i
for i in contacts_list:
  for j in deleted_list:
    if i == j:
      contacts_list.remove(i)

result_list = []
for i in contacts_list:
  test_str = i[5]
  regex = r"(\+7|8)(\s)?(\()?(\d{3})(\))?(\s|-)?(\d{3})?(\s|-)?(\d{2})?(\-)?(\d{2})(\s)?(\()?(\w{3}\.)?(\s)?(\d{4})?(\))?"
  subst = "+7(\\4)\\7-\\9-\\11 \\14\\16"
  result = re.sub(regex, subst, test_str, 0, re.MULTILINE)
  i[5] = result


with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list)


