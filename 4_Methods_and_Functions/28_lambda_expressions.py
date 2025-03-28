## Map():
# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
def square(num):
    return num**2

my_nums = [1,2,3,4,5]
my_list = list(map(square, my_nums))

print(my_list)
for item in map(square, my_nums):
    print(item)
    

print('------------------------------------------')
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN!'
    else:
        return mystring[0]      # Return the first letter if the word/string is odd
    
my_names = ['Andy', 'Eve', 'Sally']

my_list = list(map(splicer, my_names))
print(my_list)


print('------------------------------------------')
## Filter()
# The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.


def check_even(num):
    return num % 2 == 0     # Returns True or False

my_nums = [1,2,3,4,5,6]
my_list = list(filter(check_even, my_nums))
print(my_list)

for n in filter(check_even, my_list):
    print(n)


print('------------------------------------------')
## Lambda
# A lambda function is a small anonymous function, a lambda function can take any number of arguments, but can only have one expression.

lambda_function_result = lambda num: num ** 2

print(lambda_function_result(5))


print('------------------------------------------')
## Mixing Lambdas, Filter and Maps 
# We can mix these to achieve a better functionality without needing to define functions that'll only be used once

lambda_function2 = list(map(lambda num: num ** 2, my_nums))     # We are using the Lambda to use a function within a single line expression and using the my_nums list as parameters
print(lambda_function2)                                     # After this we store the results in a list and print out the list


print('------------------------------------------')
numbers_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
boolean_results = list(map(lambda num: num % 2 == 0, numbers_list))
filtered_number_results = list(filter(lambda num: num % 2 == 0, numbers_list))

print(boolean_results)
print(filtered_number_results)


print('------------------------------------------')
first_letters = list(map(lambda name: name[0], my_names))
print(first_letters)


## In short, what each of these functions and the Lambda does is:
# Lambda: Creates anonymous functions (functions without a name) for short, one-line operations.
# Filter: Filters elements of an iterable based on a condition, returning only those that satisfy the condition.
# Map: Applies a function to all elements of an iterable, returning a new iterable with the results, it the exact values generated and returned from the Function, unlike the filter.