row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)
    

def user_choice():
    user_input_value = None

    while not type(user_input_value) == int:
        try:
            user_input_value = input('Select a number for the position: ')
            user_input_value = int(user_input_value)
            if user_input_value not in range(1,4):
                print("Please choose between 1 and 3")
                user_input_value = None
        except:
            print('Not a number, try again.')



    row1[user_input_value-1] = 'X'

row2[1] = 'X'

def game():
    user_choice()
    display(row1, row2, row3)

game()