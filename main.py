from pprint import pprint
import csv
import re


with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def format_contacts_list(contacts_list):
    # Форматируем список контактов, применяя фактическую функцию format_contacts_list()
    formatted_contacts_list = []
    for contact in contacts_list:
        name = contact[0]
        organization = contact[3]
        position = contact[4]
        phone_number = contact[5]
        email = contact[6]
        # Форматируем ФИО
        parts = name.split()
        if len(parts) == 2:
            parts.append('')
        elif len(parts) == 3:
            parts = [parts[0], parts[1], ''.join(parts[2])]
        # Записываем отформатированный контакт в новый список
        formatted_contact = parts + [organization] + [position] + [phone_number] + [email]
        formatted_contacts_list.append(formatted_contact)
    return formatted_contacts_list


def delete_copy(formatted_contacts_list):
    phone_dict = dict()
    for contact in formatted_contacts_list:
        if contact[0] in phone_dict:
            value = phone_dict[contact[0]]
            for i in range(len(contact)):
                if i < len(value) and not value[i] and contact[i]:
                    value[i] = contact[i]
        else:
            phone_dict[contact[0]] = contact
    return list(phone_dict.values())

def return_number():
    old_phone_format = r"(8\s?|\+7\s?)\(?(\d+)\)?(\s|\-)?(\d+)(\s|\-)?(\d+)(\s|\-)?(\d+)"
    new_phone_format = r"+7(\2)-\4-\6-\8"
    old_add_phone_format = r"\(?(доб?)(\.?)(\s)(\d+)\)?"
    new_add_phone_format = r"доб.\4"

    for line in contacts_list:
        line[5] = re.sub(old_phone_format, new_phone_format, line[5], flags=0)
        line[5] = re.sub(old_add_phone_format, new_add_phone_format, line[5], flags=0)


formatted_contacts_list = format_contacts_list(contacts_list)
new_formatted_contacts_list = delete_copy(formatted_contacts_list)
pprint(new_formatted_contacts_list)


with open(r"phonebook_raw_new.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(new_formatted_contacts_list)