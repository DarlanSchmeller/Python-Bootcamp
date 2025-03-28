import math

# help(math)

value = 4.3434

# Floor rounds up to the integer
floor = math.floor(value)
print(floor)

# Ceil rounds the number up regardless if it's close or not to the next integer
ceil = math.ceil(value)
print(ceil)

# Round the number, default from Python
true_round = round(4.898)
print(true_round)


print('------------------------')
from math import pi

print(pi)
print(math.inf)
print(math.nan)

print('------------------------')
# Logarithmic Values with Math Module

print(math.e)
print(math.log(math.e))

print(math.log(100, 10))

print('------------------------')
# Trigonometric Functions with Math Module

print(math.sin(10))

# Convert the number into degrees
print(math.degrees(pi/2))

# Convert degrees to radians
print(math.radians(180))

print('------------------------')
# ________________________________

import random

# Return a random integer within the range specified
print(random.randint(0,100))
print(random.randint(0,1000))


# Seeds allows us to generate the same sequence of random numbers
random.seed(101)    # The value to be inserted is arbitrary

# Then the seed is used automatically to generate the same batch of numbers
print(random.randint(0,100)) # With the current seed this will always be 74
print(random.randint(0,100)) # Always 24
print(random.randint(0,100)) # Always 69
print(random.randint(0,100)) # 45, and so on..

random.seed()       # Reset seed
my_list = list(range(0,20))
print(my_list)
print(random.choice(my_list))

print('------------------------')
# ________________________________

# Sample with Replacement (value can be chosen more than once)
print(random.choices(population=my_list, k=10)) # Allows to return a list of number K randomly chosen numbers

# Sample without Replacement (value can't be chosen more than once)
print(random.sample(population=my_list, k=10))

# Shuffle List in-place (Doesn't return us anything)
random.shuffle(my_list)
print(my_list)

print('------------------------')
# ________________________________

# Random.Uniform allows us to uniformly pick a number, meaning every number between 0 and 100 has the same likelyhood of being chosen, also includes floating point numbers
print(random.uniform(0,100))

print('------------------------')
# ________________________________

# Random.Gauss allows us to generate random numbers based on a Gaussian (normal) distribution
print(random.gauss(mu=0, sigma=1))