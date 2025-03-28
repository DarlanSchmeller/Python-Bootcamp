#### Errors and Exceptions Homework

### Problem 1
# Handle the exception thrown by the code below by using try and except blocks.

try:
    for i in ['a','b','c']:
        print(i**2)

except Exception as e:
    print(f"Error caught in problem 1: {e}")


print('_______________________________')
### Problem 2
# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
try:
    x = 5
    y = 0

    z = x/y
except Exception as e:
    print(f"I caught an error at problem 2: {e}")
finally:
    print("All Done!")


print('_______________________________')
### Problem 3
# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
def ask():
    integer = None
    while not type(integer) == int:
        try:
            integer = int(input("Enter an integer number: "))
        except:
            print("Not an integer number, try again.")
        else:
            print("Integer detected!")


ask()