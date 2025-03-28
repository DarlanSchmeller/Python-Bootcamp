game_list = [1,2,3]

def display_game(game_list):
    print("Here is the current list:")
    print(game_list)

def position_choice():
    position_choice = 'Wrong'
    accepted_values = ['1', '2', '3']

    while position_choice not in accepted_values:
        choice = input("Enter a number for the desired position (1-3):  ")

        if choice not in accepted_values:
            print("Wrong choice, try again.")
        else:
            position_choice = choice

    return int(choice) - 1
            
def replacement_choice(game_list, position):
    user_placement = input("Type a string to insert at position: ")

    game_list[position] = user_placement

    return game_list

def game_on_choice():
    continue_playing = "Unsure"
    valid_choices = ['y', 'n']

    while continue_playing not in valid_choices:
        choice = input("Would you like to continue playing? (Y/N):  ").lower()
        if choice in valid_choices:
            if choice == valid_choices[0]:
                return True
            elif choice == valid_choices[1]:
                return False
            continue_playing = choice
        else:
            print('Sorry, I do not understand, try again')

    return continue_playing


game_on = True
while game_on:
    display_game(game_list)
    game_list = replacement_choice(game_list, position_choice())
    game_on = game_on_choice()