my_file = open('myfile.txt', 'w') # Opens file in write mode
my_file.write("Hello World\nThis is a new line\nThis is a third line")
my_file.close() # Closes the file, this is required so we don't run into errors

my_file = open("myfile.txt", "r")
print(my_file.read())

my_file.seek(0) # Resets the cursor, this way we can read the file's contents again
print(my_file.readlines())

with open("myfile.txt", "r") as my_file: # Best way to read a file, the with statement manages resources automatically
    text_in_file = my_file.read()
    print(text_in_file.upper()) # We don't need to close the file, the with statement does it by itself

print('------------------------------')
with open('myfile.txt', 'a') as file:
    file.write("\nThis a new line being added by Python")


# mode='w' will overwrite the file
# mode='a' will append to the end of the file
# mode='r' will read the file
# mode='r+' will read and write to the file
# mode='a+' will append and read
# mode='w+' will overwrite and read
# mode='a+' will append and read
# mode='x' will create a new file and read