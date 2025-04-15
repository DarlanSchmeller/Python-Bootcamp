# Task One: Use Python to extract the Google Drive link from the .csv file. (Hint: Its along the diagonal from top left to bottom right)
import csv

with open('./Exercise_Files/find_the_link.csv', mode='r', encoding='utf-8') as csv_file:
    csv_data = csv.reader(csv_file)
    data_lines = list(csv_data)
    print(data_lines)

    link_str = ''
    for row_num,data in enumerate(data_lines):
        link_str += data[row_num]

    print(link_str)



# Task Two: Download the PDF from the Google Drive link and find the phone number that is in the document.
# # You should get this phone number: 505 503 4455
import PyPDF4
import re

with open('Exercise_Files/Find_the_Phone_Number.pdf', mode='rb') as pdf_file:
    pdf_data = PyPDF4.PdfFileReader(pdf_file)
    print(pdf_data.numPages)

    pattern = r'\d{3}'
    all_text = ''

    for n in range(pdf_data.numPages):
        page = pdf_data.getPage(n)
        page_text = page.extractText()

        all_text = all_text + ' ' + page_text

        print(all_text)
        for match in re.finditer(pattern, all_text):
            print(match)

        print(all_text[41808:41808+11])