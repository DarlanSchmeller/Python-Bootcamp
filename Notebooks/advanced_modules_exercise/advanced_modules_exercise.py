### Objetive
# Use the Python os module and regular expressions to iterate through each file, open it, and search for a telephone number.

import os
import re

def find_phone_number():
    phone_numbers_found = []
    telephone_format = r'\d{3}-\d{3}-\d{4}'
    parent_folder = "extracted_content/"
    folders = os.listdir(parent_folder)

    for folder in folders:
        files_list = os.listdir(parent_folder + folder)

        for file in files_list:
            file_path = parent_folder + folder + '/' + file
            with open(file_path, 'r') as text_file:
                text_file_content = text_file.read()
                result = re.findall(telephone_format, text_file_content)
                if result:
                    phone_numbers_found.append(''.join(result))

    for phone_number in phone_numbers_found:
        print(phone_number)

find_phone_number()