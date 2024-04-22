from pprint import pprint
import re
import csv


def fix_name_phone(contacts_list):
  for contact in contacts_list:
    test_str = contact[5]
    regex = r"(\+7|8)(\s)?(\()?(\d{3})(\))?(\s|-)?(\d{3})?(\s|-)?(\d{2})?(\-)?(\d{2})(\s)?(\()?(\w{3}\.)?(\s)?(\d{4})?(\))?"
    subst = "+7(\\4)\\7-\\9-\\11 \\14\\16"
    result = re.sub(regex, subst, test_str, 0, re.MULTILINE)
    contact[5] = result
    if len(contact[0]. split()) > 2:
      contact[1]=(contact[0].split()[1])
      contact[2]=(contact[0].split()[2])
      contact[0]=(contact[0].split()[0])
    elif len(contact[0].split()) == 2:
      contact[1]=(contact[0].split()[1])
      contact[0]=(contact[0].split()[0])
    elif len(contact[1].split()) > 1:
      contact[2]=(contact[1].split()[1])
      contact[1]=(contact[1].split()[0])
  return contacts_list

def fix_double(contacts_list):   
  contact1 = contacts_list[0]
  deleted_list = []
  for contact in sorted(contacts_list[1:len(contacts_list)]):
    if contact[0:2] == contact1[0:2]:
      for ind in range(1,7):
        if contact1[ind]:
          contact[ind] = contact1[ind]
      deleted_list.append(contact1)
    contact1 = contact
  for contact in contacts_list:
    for contact_del in deleted_list:
      if contact == contact_del:
        contacts_list.remove(contact)
  return contacts_list

if __name__ == '__main__':
  
  with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

  contacts_list = fix_name_phone(contacts_list)
  contacts_list = fix_double(contacts_list)
  
  with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)

