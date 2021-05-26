from pprint import pprint

import csv
import re

with open('phonebook_raw.csv', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

new_contacts_list = [['lastname', 'firstname', 'surname', 'phone']]
for contact in contacts_list[1:]:
    temp = []

    client = ' '.join(contact[:3])
    client = re.search(r'(\w+)\s(\w+)\s(\w+)?', client)
    if client.group(3):
        temp.append(client.group(1))
        temp.append(client.group(2))
        temp.append(client.group(3))
    else:
        temp.append(client.group(1))
        temp.append(client.group(2))

    number = contact[5]
    number = re.search(r'(\+7|8)?\s?\(?(\d{3})\)?\s?-?(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})(.+доб.+(\d{4}))?', number)
    if number:
        phone = f'+7({number.group(2)}){number.group(3)}-{number.group(4)}-{number.group(5)}'
        if number.group(7):
            phone += f' доб.{number.group(7)}'
        temp.append(phone)

    pprint(temp)

    is_copy = False
    for i in range(len(new_contacts_list)):
        if new_contacts_list[i][0] == temp[0] and new_contacts_list[i][1] == temp[1]:
            is_copy = True
            if len(temp) > len(new_contacts_list[i]):
                new_contacts_list[i] = temp

    if is_copy is False:
        new_contacts_list.append(temp)

with open('phonebook.csv', 'w', encoding='utf-8', newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_contacts_list)
