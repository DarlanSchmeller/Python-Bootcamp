## Python looks for names (variables or functions) in different scopes using the LEGB rule:

# L (Local): The current function's scope.
# E (Enclosing): The scope of any enclosing functions.
# G (Global): The module-level scope.
# B (Built-in): The built-in scope that contains Python's built-in functions and exceptions.


x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())

print('-------------------------------------------')
## Local Example:
# In the example below, the variable 'num' is local to the Lambda, it can't be accessed outside the Lambda.

y = lambda num: num % 2 == 0

print(y(10))


print('-------------------------------------------')
## Enclosed Local Example:
# In this example, we show the order in which python searches for variables and objects in the namespace, first it looks for the definition inside the local scope
# Then it moves on to the enclosed scope, which is the outer function from a function inside a function
# Lastly it looks for the Global definition of the object you're attempting to refer to

# GLOBAL
name = 'THIS IS A GLOBAL STRING'

def greet():
    # ENCLOSING
    name = 'Sammy'
    
    def hello():
        # LOCAL
        name = 'IM A LOCAL'

        print('Hello ' + name)
    hello()


greet()


print('-------------------------------------------')
## Built-In
# This scope is basically the functions and objects that come built-in within Python

# help(len) # This function tells us what Python knows about an object, in this case he tells us this is a built-in function


print('-------------------------------------------')
# GLOBAL ASSIGNMENT
x = 50

def func():
    global x    # This tells the function to look for the variable X in the Global Scope and use it from now on
    print(f"X is {x}") # However, using the global variable means that the global variable will now change if the variable value changes inside the function
    
    # LOCAL REASSIGNMENT
    x = 200
    print(f'I JUST LOCALLY CHANGED X TO {x}') # The global X is now 200 since the function is using the global variable X and modifying it directly

func() 
