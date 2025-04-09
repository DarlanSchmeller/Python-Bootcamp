import csv

data = open('example.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)
print(data_lines)
print('\n')
print(data_lines[0])
print(data_lines[1])
print(data_lines[1][1])
print(len(data_lines))


print('\n')

#   Get all emails from a colum
all_emails = []

for line in data_lines[1:10]:
    email = line[3]
    all_emails.append(email)

for email in all_emails:
    print(email)

print('\n')

#   Get all full names from the CSV file
full_names = []

for line in data_lines:
    full_names.append(line[1] + ' ' + line[2])

    #   Alternative way to do this with join()
    # dog = ' '.join(line[1:3])
    # print('dog')
    # print(dog)

for name in full_names:
    print(name)

data.close()


print('--------------------------------------------')

#    Writing to a CSV file
file_to_output = open('to_save_file.csv', mode='w', newline='',encoding='utf-8')    #  Open File in Writing Mode

csv_writer_file = csv.writer(file_to_output, delimiter=',')
csv_writer_file.writerow(['a','b','c'])
csv_writer_file.writerows([['1','2','3'], ['4','5','6']])

file_to_output.close()

appending_file = open('to_save_file.csv', mode='a', newline='',encoding='utf-8')    #  Open File in Appending Mode
csv_writer_appending_file = csv.writer(appending_file, delimiter=',')
csv_writer_appending_file.writerow(['21','334','24'])
csv_writer_appending_file.writerow(['566','13','455'])
appending_file.close()

with open('to_save_file.csv', mode='r', encoding='utf-8') as written_file:
    print(written_file.read())