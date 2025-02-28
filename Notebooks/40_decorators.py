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

