f = open('fileone.txt', 'w+', encoding='utf-8')
f.write('ONE FILE')
f.close()

f = open('filetwo.txt', 'w+', encoding='utf-8')
f.write('TWO FILE')
f.close()

#______________________________________________

# Inbuilt Module used for compressing files
import zipfile

# Creates zip file
comp_file = zipfile.ZipFile('comp_file.zip', 'w')

# Compresses the two files into the zip file we created
comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)

comp_file.close()


#______________________________________________

# Extracting the content of the zip file

zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
zip_obj.extractall()


#----------------------------------------------

# Using Shell Utilities to Zip an entire folder

import shutil
directory_to_zip = '/home/dev/Desktop/Python-Bootcamp/MyMainPackage'
output_filename = 'example'

shutil.make_archive(output_filename, 'zip', directory_to_zip)

# Using Shell Utilities to unzip the zip file

shutil.unpack_archive('example.zip', 'final_unzip', 'zip')