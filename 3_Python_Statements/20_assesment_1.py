st = "print only the words that start with s in this sentence"

# code below

words = st.split()
print(type(words))

for word in words:
    if word[0].lower() == 's':
        print(word)




print('-----------------------------')
# print all the even numbers from 0 to 10 using range()

for num in range(0,11):
    if num % 2 == 0:
        print(num)

print('-----------------------------')
# Use list comprehension to create a list of all numbers between 1 and 50 that are divisible by 3

mylist = [x for x in range(1,51) if x % 3 == 0]
print(mylist)

print('-----------------------------')
# Go through the String below and if the length of the Word is even, print even!

st = 'Print every word in this sentence that has an even number of letters'


for word in st.split():
    if len(word) % 2 == 0:
        print(f"'{word}' is EVEN!")

print('-----------------------------')
# Write a program that prints the integers from 1 to 100. But for multiples of Three print "Fizz" instead of the number. and for multiples of five print "Buzz". For numbers
# which are multiples of both three and five print "FizzBuzz"

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
        
print('-----------------------------')
# Use list comprehension to create a list of the first letters of every word in the string below
st = 'Create a list for the first letters of every word of this string'

mylist = [word[0] for word in st.split()]
print(mylist)