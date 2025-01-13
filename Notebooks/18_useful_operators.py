for num in range(3,10):
    print(num)

print('------------------------------')
my_list =list(range(0,11,2)) # We can use range to create lists
print(my_list)

print('------------------------------')
index_count = 0

for letter in 'abcde': # Common method of doing this
    print(f"At index {index_count} the letter is {letter}")
    index_count += 1

print('------------------------------')
word = 'abcde'

for index,letter in enumerate(word):
    print(f"At index {index} the letter is {letter}.")

# The enumerate object yields pairs containing a count (from start, which defaults to zero) and a value yielded by the iterable argument.
# enumerate is useful for obtaining an indexed list:

print('------------------------------')
my_list1 = [1,2,3]
my_list2 = ['a','b','c']

for item in zip(my_list1,my_list2):
    print(item)

print('------------------------------')
print('x' in [1,2,3]) # This method allows us to verify if an item is in a list
print('x' in ['x','y','z'])
print('a' in 'Hello World')
print('a' in 'In a World')

print('mykey' in {'mykey': 345}) # Verifies if the value is in a key
print(345 in {'mykey': 345}.values()) # Verify if the item is in a value

print('------------------------------')
print(min([1,2,3,4,5])) # Returns the lowest value in a list
print(max([1,2,3,4,5])) # Returns the maximum value in a list

print('------------------------------')
from random import shuffle # Allows us to Scramble a list

mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist) # In place function, doesn't return anything, only the list is affected with the changes
print(mylist) # Will print the Scrambled List

print('------------------------------')
from random import randint # Allows to pick a random integer

print(randint(0,100))

print('------------------------------')
name = input("Write your name: ")
print("Name found: " + name)