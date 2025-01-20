
# Problems are arranged in increasing difficulty:
# * Warmup - these can be solved using basic comparisons and methods
# * Level 1 - these may involve if/then conditional statements and simple methods
# * Level 2 - these may require iterating over sequences, usually with some kind of loop
# * Challenging - these will take some creativity to solve


# ===============================================================================================
# ===============================================================================================

# ## WARMUP SECTION:

# ===============================================================================================
# #### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd

def lesser_two_evens(num1=3, num2=2):
    if (num1 % 2 == 0) and (num2 % 2 == 0):
        if num1 < num2:
            return num1
        else:
            return num2
    else:
        if num1 > num2:
            return num1
        else:
            return num2

print(lesser_two_evens())

# ===============================================================================================
# #### ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(string):
    word1, word2 = string.lower().split()
    
    if word1[0] == word2[0]:
        return True
    else:
        return False

print(animal_crackers('Two Things'))


# ===============================================================================================
# #### MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 *or* if one of the integers is 20. If not, return False

def two_integers(int1,int2):
    if sum([int1,int2]) == 20:
        return True
    elif int1 == 20 or int2 == 20:
        return True
    else:
        return False
    
print(two_integers(10,10))


# ===============================================================================================
# ===============================================================================================

# # LEVEL 1 PROBLEMS

# ===============================================================================================
# #### OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
     
def old_macdonald(name):
    final_word = ''

    for index,letter in enumerate(name):
        if index == 0 or index == 3:
            final_word = final_word + letter.upper()
        else:
            final_word = final_word + letter

    return final_word


print(old_macdonald('macdonald'))

# ===============================================================================================
# #### MASTER YODA: Given a sentence, return a sentence with the words reversed
#     master_yoda('I am home') --> 'home am I'
#     master_yoda('We are ready') --> 'ready are We'

def master_yoda(sentence):
    words_list = sentence.split()
    words_list.reverse()

    return ' '.join(words_list)

print(master_yoda('I am home'))


# ===============================================================================================
# #### ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# 
# Example Output:
#     almost_there(90) --> True
#     almost_there(104) --> True
#     almost_there(150) --> False
#     almost_there(209) --> True
    
def almost_there(n):
    if n in range(90,111):
        return True
    elif n in range(190,211):
        return True
    else:
        return False

print(almost_there(209))


# ===============================================================================================
# ===============================================================================================

# # LEVEL 2 PROBLEMS

# ===============================================================================================
# #### FIND 33: 
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def find_33(list):
    for index in range(len(list)-1):
        if list[index] == 3:
            if list[index+1] == 3:
                return True

    return False

print(find_33([1,4,3,3]))


# ===============================================================================================
# #### PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
#     paper_doll('Hello') --> 'HHHeeellllllooo'
#     paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'


def paper_doll(sentence):
    final_word = ''

    for letter in sentence:
        final_word = final_word + letter*3

    return final_word

print(paper_doll('Hello'))


# ===============================================================================================
# #### BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 *and* there's an eleven,
# reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
#     blackjack(5,6,7) --> 18
#     blackjack(9,9,9) --> 'BUST'
#     blackjack(9,9,11) --> 19

def blackjack(num1,num2,num3):
    numbers_sum = sum([num1,num2,num3])
    
    if numbers_sum <= 21:
        return numbers_sum
    elif numbers_sum > 21 and 11 in [num1,num2,num3]:
        return numbers_sum - 10
    elif numbers_sum > 21:
        return 'BUST'

print(blackjack(15,20,12))

# ===============================================================================================
# #### SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting 
# with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers. 
#     summer_69([1, 3, 5]) --> 9
#     summer_69([4, 5, 6, 7, 8, 9]) --> 9
#     summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(list=[2, 1, 6, 9, 11]):
    new_list = []
    six_found = False

    for number in list:
        if number == 6:
            six_found = True
        elif number == 9:
            six_found = False
        elif six_found == False:
            new_list.append(number)

    sum_output = sum(new_list)
    return sum_output

print(summer_69())

# ===============================================================================================
# ===============================================================================================

# # CHALLENGING PROBLEMS

# ===============================================================================================
# #### SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#      spy_game([1,2,4,0,0,7,5]) --> True
#      spy_game([1,0,2,4,0,5,7]) --> True
#      spy_game([1,7,2,0,4,5,0]) --> False


def spy_game(list = [1,2,4,0,0,7,5]):
    list_records = []

    for item in list:
        if item == 0 or item == 7:
            list_records.append(str(item))

    if list_records:                        # If the list has items proceed
        new_list = ''.join(list_records)

        if '007' in new_list:
            print('007 Was Found!')
            return True
        else:
            return False
    
spy_game()

# ===============================================================================================
# #### COUNT PRIMES: Write a function that returns the *number* of prime numbers that exist up to and including a given number
#     count_primes(100) --> 25

# By convention, 0 and 1 are not prime.


def count_primes(num=100):
    if num < 2:
        return 0
    
    prime_numbers = [2]
    x = 3

    while x <= num:
        for y in range(3,x,2):
            if x%y == 0:
                x += 2
                break
        else:
             prime_numbers.append(x)
             x += 2
        
    return len(prime_numbers)
    
print(count_primes())

# ===============================================================================================
