mystring = 'Hello World'

print(mystring[1]) # prints second letter of the string, count begins at 0
print(mystring[-1]) # prints last letter of string, python supports negative indexing


mystring = 'abcdefghijk'
print(mystring[2:])
print(mystring[0:5])
print(mystring[0:3])
print(mystring[3:6]) # go up to 6 but don't include the character at pos 6

print(mystring[::2]) # Third parameter is step

print(mystring[::-1]) # Reverse your string

