# Iterators and Generators Homework
# Problem 1
# Create a generator that generates the squares of numbers up to some number N.
print("Problem 1: \n")

def square_generator(n):
    for number in range(1, n):
        yield number * number


for item in square_generator(10):
    print(item)


print("---------------------------------------------")
# ___________________________________________________
# Problem 2
# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
# Note: Use the random library. For example:
print("Problem 2: \n")

import random

def random_generator(low_number, high_number):
    for n in range(high_number):
        yield random.randint(low_number, high_number)


for item in random_generator(1,10):
    print(item)


print("---------------------------------------------")
# ___________________________________________________
# Problem 3
# Use the iter() function to convert the string below into an iterator:
print("Problem 3: \n")

s = 'hello'
iterable_s = iter(s)
print(next(iterable_s))



print("---------------------------------------------")
# ___________________________________________________
# Problem 4
# Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.
print("Problem 4: \n")



print("""A use case would be in which there is no need to store the data into memory 
      \n yielding allows the system to only output the values which allows the user to only iterate through it""")





print("---------------------------------------------")
# ___________________________________________________
# Extra Credit!
# Can you explain what gencomp is in the code below? (Note: We never covered this in lecture! You will have to do some Googling/Stack Overflowing!)
print("Problem 5: \n")

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)

print("\n \t Reply: Creates a list from only approved values using generator comprehension")

# Hint: Google generator comprehension!