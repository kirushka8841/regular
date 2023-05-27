import re
from pprint import pprint
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

def extract_phone_numbers(text):
    regex = r"(\+7|8)[\- ]?(\()?(\d{3})(\))?[\- ]?(\d{3})[\- ]?(\d{2})[\- ]?(\d{2})( доб\.\d{1,4})?"
    phone_numbers = []
    for match in re.finditer(regex, text):
        phone_number = "+7({}){}-{}-{}".format(match.group(3), match.group(5), match.group(6), match.group(7))
        if match.group(8):
            phone_number += " {}".format(match.group(8))
        phone_numbers.append(phone_number)
    return ", ".join(phone_numbers)


def format_contacts_list(contacts_list):
    # Форматируем список контактов, применяя фактическую функцию format_contacts_list()
    formatted_contacts_list = []
    for contact in contacts_list:
        name = contact[0]
        organization = contact[3]
        position = contact[4]
        phone_number = contact[5]
        email = contact[6]
        formatted_phone_number = extract_phone_numbers(phone_number)
        # Форматируем ФИО
        parts = name.split()
        if len(parts) == 2:
            parts.append('')
        elif len(parts) == 3:
            parts = [parts[0], parts[1], ''.join(parts[2])]
        # Записываем отформатированный контакт в новый список
        formatted_contact = parts + [organization] + [position] + [formatted_phone_number] + [email]
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


formatted_contacts_list = format_contacts_list(contacts_list)
new_formatted_contacts_list = delete_copy(formatted_contacts_list)
pprint(new_formatted_contacts_list)