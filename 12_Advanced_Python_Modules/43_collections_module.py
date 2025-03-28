# 1- Counter from Collections, allows us to count the instances of the same value in an object
from collections import Counter
mylist = [1,1,1,1,1,2,2,2,2,2,4,4,4,4,5,5,5,6,6,6,7,7]

print(Counter(mylist))

sentence = "How many times does each word show up in this sentence with a word"
split_sentence = sentence.split()
print(Counter(split_sentence))

print("-------------------------------")

letters = 'aaaaaaaabbbbbccccccdddd'

c = Counter(letters)
print(c.most_common(1))

print("-------------------------------")
from collections import defaultdict

# This component adds a default value in an instance where a key error would occur in a dictionary
d = {'a':10}

d = defaultdict(lambda: 0)
print(d['dog'])     # This key doesn't exist



print("-------------------------------")
from collections import namedtuple

# Allows us to create a Tuple with named indexes, similar to OOP
Dog = namedtuple('dog',['age','breed','name'])
sammy = Dog(age=5, breed='Husky', name='Sam')
print(sammy)
