def add_function(num1 : int = 1, num2 : int = 1):
    """
    Simple Function that Adds two
    Numbers Together/
    """
    return (num1 + num2)

results = add_function(1,2)
print(results)

print('-------------------------------')
def say_hello():
    print("Hello")
    print("How")
    print("Are")
    print("You?")

say_hello()

print('-------------------------------')
def say_hello(name= 'User'):
    print(f"Hello {name}, how are you?")

say_hello('Darlan')

print('-------------------------------')
def add_num(num1,num2):
    return (num1+num2) # Allows us to store this value in a variable for later usage

results = add_num(3,4)
print(results)