x = 0

while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1
    
    # Break, Continue and Pass statements
    # Break: Breaks out of the current loop
    # Continue: Goes to the top of the closest, enclosing loop
    # Pass: Does nothing

print('------------------------------')
x = [1,2,3]

for number in x:
    pass # Does nothing and doesn't break the code flow

print('end of program')

print('------------------------------')
mystring = "Sammy"

for letter in mystring:
    if letter == 'a':
        continue # Will continue so it will not print 'a'
    if letter == 'y':
        break # Stops loop
    print(letter)