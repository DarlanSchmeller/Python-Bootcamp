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

    # ALTERNATE METHOD BELOW
    print("-------------------------------")

    for folder, sub_folders, files in os.walk(os.getcwd() + '/extracted_content'):
        for file in files:
            with open(folder + '/' +file,'r') as f:
                text = f.read()

            second_result = re.findall(phone_number, text)
            if second_result:
                print(''.join(second_result))

find_phone_number()