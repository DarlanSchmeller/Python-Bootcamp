# *args: It's a way to set the function's arguments to use a Tuple that can store as many arguments as you need
# **kwargs: It's a method to set the function's arguments to store as many keywords inside a dictionary as you need


# *args (Positional Arguments)
# *args allows you to pass a variable number of positional arguments to a function.
# The arguments are passed as a tuple, which means that inside the function, args will be treated like a tuple containing all the extra arguments passed.


# 2. **kwargs (Keyword Arguments)
# **kwargs allows you to pass a variable number of keyword arguments to a function. These are arguments passed as key-value pairs (i.e., named arguments).
# Inside the function, kwargs will be treated as a dictionary, where the keys are the argument names and the values are the corresponding values passed in.


def myfunc(a, b, c=0,d=0,e=0): 
    # Returns 5% of the sum of A and B
    return sum((a,b,c,d,e)) * 0.05

print(myfunc(40,60,100,100)) # When we set parameters like this we can only set a limited amount of arguments


print('-------------------------------------')
def myfunc(*args): # This allows us to use as many Number arguments as we need, it'll be treated as a Tuple inside the Function
    for item in args:
        print(item)
    print('---')
    print('5% of the Sum of args:')
    return sum(args) * 0.05

print(myfunc(40,60,100,1,34)) # When using *args we can pass as many arguments as we want

print('-------------------------------------')
def myfunc(**kwargs): # Uses a dictionary to store unlimited arguments
    print(kwargs)

    if 'fruit' in kwargs:
        print('My fruit of choice is: ' + kwargs['fruit'])
    else:
        print('I did not find anything.')

myfunc(fruit="apple", veggie = 'lettuce')


def myfunc(*args, **kwargs):
    print(f"I would like  {args[0]}  {kwargs['food']}")

myfunc(10,20,30, fruit="orange", food="eggs") # We can use both *args and **kwargs, as long as we pass them in the order we defined, in this case all args first then all kwargs
