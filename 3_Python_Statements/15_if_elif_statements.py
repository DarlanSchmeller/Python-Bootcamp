import random

if True:
    print("It's True!")
if 3 > 2:
    print("It's True, 3 is greater than 2!")

print("------------------------------")
hungry = random.choice([True, False])

if hungry:
    print("I am hungry! Feed me!")
else:
    print("I am not hungry.")

print('------------------------------')
loc = random.choice(['Bank', 'Auto Shop','Store', 'Unknown'])

if loc == "Auto Shop":
    print("Cars are nice!")
elif loc == "Bank":
    print("Money is amazing!")
elif loc == "Store":
    print("Welcome to my store!")
else:
    print("I don't know the location.")
    
print('------------------------------')
name = random.choice(['Sammy', 'Frank','Ryan', 'Unknown'])

if name == "Sammy":
    print("Hello Sammy!")
elif name == "Frank":
    print("Hello Frank!")
elif name == "Ryan":
    print("Hello Ryan!")
else:
    print("I don't know your name.")