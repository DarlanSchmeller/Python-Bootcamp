def func():
    return 1

def hello(name='Jose'):
    print("The hello function has been executed!")
    
    def greet():
        return "\t This is the greet function inside hello!"
    print(greet())
    
    def welcome():
        return '\t This is welcome() inside hello!'
    print(welcome())

    print("I am going to return a function!")

    if name == "Jose":
        return greet
    else:
        return welcome

returned_function = hello("Jose")

print('-------')
print(type(returned_function))
print(returned_function())
print('-------')

def cool():
    def super_cool():
        return 'I am very cool!'
    return super_cool

some_func = cool()

def other(some_def_func):
    print("Other code runs here:")
    print(some_def_func())

other(some_func)

print("--------------------------")

def new_decorator(original_func):
    def wrap_func():
        print("Some extra code, before the original function")
        original_func()
        print("Some extra code, after the original function")
    return wrap_func()


def func_needs_decorator():
    print("I want to be decorated!!")

decorated_function = new_decorator(func_needs_decorator)
decorated_function


print("--------------------------")
# Easier Syntax for defining a decorator
@new_decorator
def func_needs_decorator():
    print("I want to be decorated!!")


func_needs_decorator