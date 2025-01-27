row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)
    

def user_choice():
    # VARIABLES
    
    # Initial
    choice = 'WRONG'
    acceptable_range = range(0,10)
    within_range = False

    while choice.isdigit() == False or within_range == False:
        
        choice = input('Select a number for the position: ')

        # Digit Check
        if choice.isdigit() == False:
            print("Sorry that is not a digit.")

        # Range Check
        if choice.isdigit():
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Number entered not in the correct range")
                within_range = False
    return int(choice)


row2[1] = 'X'

def game():
    user_chosen_position = user_choice()
    row1[user_chosen_position] = 'X'
    display(row1, row2, row3)

game()