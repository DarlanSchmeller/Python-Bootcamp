### Advanced Python Objects Test
# Problem 1: Convert 1024 to binary and hexadecimal representation

print('Binary representation:',bin(1024))
print('Hexadecimal representation:',hex(1024))

 


     
# ----------
# Problem 2: Round 5.23222 to two decimal places
print(round(5.23222, 2))

 



# ----------------------------------------------------------------------------------------------------     
### Advanced Strings
# Problem 3: Check if every letter in the string s is lower case
print('\n\t ------------------ \n')

s = 'hello how are you Mary, are you feeling okay?'
answer = s.islower()

print(f"Are all letters in the phrase: {s} lowercase? The answer is... {answer}")



     
# ----------
# Problem 4: How many times does the letter 'w' show up in the string below?


s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
w_amount = s.count('w')
print(f"The letter 'w' shows up {w_amount} times in the string: {s}")


# ----------------------------------------------------------------------------------------------------     

### Advanced Sets
# Problem 5: Find the elements in set1 that are not in set2:
print('\n\t ------------ \n')


set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
sets_difference = set1.difference(set2)

print(f'The difference between {set1} and {set2} is: ')
print(sets_difference)


     
# ----------
# Problem 6: Find all elements that are in either set:

union_set = set1.union(set2)
print(f'The intersection between {set1} and {set2} is: ')
print(union_set)



# ----------------------------------------------------------------------------------------------------     

### Advanced Dictionaries
# Problem 7: Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using a dictionary comprehension.
print('\n\t ------------ \n')

problem_dictionary = {x: x**3 for x in range(5)}
print(problem_dictionary)


# ----------------------------------------------------------------------------------------------------     

### Advanced Lists
# Problem 8: Reverse the list below:
print('\n\t ------------ \n')


list1 = [1,2,3,4]

print('Reverse the list below:')
print(list1)

list1.reverse()
print(list1)

# ----------
# Problem 9: Sort the list below:


list2 = [3,4,2,5,1]


print('Sort the list below:')
print(list2)

list2.sort()
print(list2)