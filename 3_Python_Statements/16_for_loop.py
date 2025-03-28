my_list = ['one','two','three']

for item in my_list:
    print(item)

print('------------------------------')
another_list = [1,2,3,4,5,6,7,8,9,10]

for number in another_list:
    if number % 2 == 0:
        print(number)

print('------------------------------')
for i in range(1,4):
    print(i)

print('------------------------------')
list_sum = 0
for number in another_list:
    list_sum = list_sum + number
print(list_sum)

print('------------------------------')
for letter in "Hello World":
    print(letter)

print('------------------------------')
for _ in "Hello World": # If you don't use a variable, you can use an underscore as common practice to improve readability
    print("Cool") # prints for each letter of the string

print('------------------------------')
my_tuple = (1,2,3)

for tup in my_tuple:
    print(f'Tuple value: {tup}')

print('------------------------------')
my_list_tuples = [(1,2), (3,4), (5,6), (7,8)]

for item in my_list_tuples:
    print(item)

print('------------------------------')
my_list_tuples = [(1,2), (3,4), (5,6), (7,8)]

for a,b in my_list_tuples: # Tuple Unpacking
    print(a)
    print(b)

print('------------------------------')
my_list_tuples = [(1,2,3), (4,5,6), (7,8,9), (10,11,12)]

for a,b,c in my_list_tuples:
    print(a)
    print(b)
    print(c)

print('------------------------------')
d = {'k1':1, 'k2':2, 'k3':3}

for key, value in d.items():
    print(key)
    print(value)