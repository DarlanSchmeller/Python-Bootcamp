from random import shuffle

example = [1,2,3,4,5,6,7]

shuffle(example)
print(example)

print('-------------------------------')
def shuffle_list(my_list):
    """
    Shuffles and returns a list

    """
    shuffle(my_list)
    return my_list

my_list = [1,2,3,4,5,6,7,8,9,10]
print(shuffle_list(my_list))

print('-------------------------------')
my_list = [' ', 'O', ' ']

def player_guess():
    """
    Allows user to guess a position
    for finding an O string in a list
    """
    guess = ''

    while guess not in [0,1,2]:
        guess = int(input("Which position would you like to guess? 0, 1 or 2: "))
    return int(guess)

def check_guess(mixed_list, guess):
    if mixed_list[guess] == 'O':
        print('Correct!')
    else:
        print('Wrong guess!')

mixed_list = shuffle_list(my_list)

user_guess = player_guess()
check_guess(mixed_list, user_guess)
print(my_list)

