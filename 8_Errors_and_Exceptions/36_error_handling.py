def add(n1,n2):
    number1 = int(n1)
    number2 = int(n2)
    return number1 + number2

try:
    # Want to attempt this code
    user_value_1 = input("Enter the first number: ")
    user_value_2 = input("Enter the second number: ")
    result = add(user_value_1, user_value_2)
except Exception as e:
    # Execute this code if an error is encontered
    print(f"Error found: {e}")
    pass
else:
    print("Add went well!")
    print(result)

print("This should get printed regardless of error")


print('------------------------------')
#______________________________________

try:
    with open('testfile.txt','w') as f:
        f.write('Text written from notebook n°36.')
except TypeError as e:
    print(f"I found a TypeError: {e}")
except OSError as e:
    print(f"Hey you! We caught an OS Error: {e}")
else:
    print("I only run if there's no errors!")
finally:
    print("I always run!")