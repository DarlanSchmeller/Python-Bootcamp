# # Functions and Methods Homework 

# Complete the following questions:
print('--------------------------------------------------------------------------------')
# _________________________________________________________________________________________________________________________
# **Write a function that computes the volume of a sphere given its radius.**
# The volume of a sphere is given as 4/3 πr3

def vol(rad):
    return (4/3) * (3.14) * (rad**3)

print(vol(2))


print('--------------------------------------------------------------------------------')
# _________________________________________________________________________________________________________________________
# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
    if num in range(low-1, high+1):
        return f"{num} is in the desired range"
    else:
        return "Number is not in range."


# Check
print(ran_check(8, 2, 7))


print('--------------------------------------------------------------------------------')
# _________________________________________________________________________________________________________________________
# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

#     Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#     Expected Output : 
#     No. of Upper case characters : 4
#     No. of Lower case Characters : 33

# HINT: Two string methods that might prove useful: **.isupper()** and **.islower()**

def up_low(s):
    upper_count = 0
    lower_count = 0

    for letter in s:
        if letter.isupper():
            upper_count += 1
        elif letter.islower():
            lower_count += 1 
        else:
            pass

    return upper_count, lower_count

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
upper, lower = up_low(s)
print(f"No. of Upper case characters : {upper}")
print(f"No. of Lower case Characters : {lower}")


print('--------------------------------------------------------------------------------')
# _________________________________________________________________________________________________________________________
# Write a Python function that takes a list and returns a new list with unique elements of the first list.

#     Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
#     Unique List : [1, 2, 3, 4, 5]

def unique_list(provided_list):
    return list(set(provided_list))

    # unique_list = []

    # for item in list:
    #     if item in unique_list:
    #         pass
    #     else:
    #         unique_list.append(item)
    # return unique_list

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))           


print('--------------------------------------------------------------------------------')
# _________________________________________________________________________________________________________________________
# **Write a Python function to multiply all the numbers in a list.**
#     Sample List : [1, 2, 3, -4]
#     Expected Output : -24


def multiply_list(list):
    result = 1

    for number in list:
        result = number * result

    return result

print(multiply_list([1, 2, 3, -4]))




print('--------------------------------------------------------------------------------')
# _________________________________________________________________________________________________________________________
# **Write a Python function that checks whether a word or phrase is palindrome or not.**

# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.
# def palindrome(s):
#     pass
# palindrome('helleh')

def palindrome(word):
    reverse_word = word[::-1]

    if reverse_word == word:
        return 'Palindrome Detected'
    else:
        return 'No palindrome found'

print(palindrome("helleh"))


print('--------------------------------------------------------------------------------')
# _________________________________________________________________________________________________________________________
# #### Hard:

# **Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)**

#     Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#     For example : "The quick brown fox jumps over the lazy dog"

# Hint: You may want to use .replace() method to get rid of spaces.
# Hint: Look at the [string module](https://stackoverflow.com/questions/16060899/alphabet-range-in-python)
# Hint: In case you want to use [set comparisons](https://medium.com/better-programming/a-visual-guide-to-set-comparisons-in-python-6ab7edb9ec41)
# import string

def pangram(string):
    clean_string = string.replace(' ', '').lower()

    alphabet_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for letter in alphabet_letters:
        if letter in clean_string:
            pass
        elif letter not in clean_string:
            return 'Not a Pangram'
    return 'String is a Pangram'
    
print(pangram('The quick brown fox jumps over The lazy dog'))