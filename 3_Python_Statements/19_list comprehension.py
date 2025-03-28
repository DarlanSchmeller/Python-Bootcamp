mystring = 'Hello'
mylist = [letter for letter in mystring]

# for letter in mystring:
#     mylist.append(letter)

print(mylist)

print('------------------------------')
mylist = [x for x in 'word'] # Basically a for loop inside a list that appends each letter into the list

print(mylist)

print('------------------------------')
mylist = [x for x in range(0,11)]
print(mylist)

mylist = [x for x in range(0,11) if x % 2 == 0]
print(mylist)

mylist = [num**2 for num in range(0,11)]
print(mylist)

print('------------------------------')
celcius = [0,10,20,34.5]

fahrenheit = [ ( (9/5) * temp + 32) for temp in celcius] # same as below
print(fahrenheit)

fahreinheit2 = []

for temp in celcius:
    fahreinheit2.append(( (9/5) *temp + 32))
print(fahreinheit2)

print('------------------------------')
results = [x if x%2==0 else f'{x} is ODD' for x in range(0,11)]

print(results)

print('------------------------------')

mylist = []

for x in [2,4,5]:
    for y in [100,200,300]:
        mylist.append(x*y)

print(mylist)

mylist = [x*y for x in [2,4,5] for y in [100,200,300]] # Same as above, just a way to do it with list comprehension
print(mylist)