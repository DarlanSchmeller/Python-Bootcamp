myset = set() # sets are similar to lists, but their values are unique, the set itself is unordered

myset.add(1)
myset.add(2)
print(myset)

mylist = [1,1,31,34,54,4,3,3,4,1]
mylist = set(mylist)
print(mylist)
print(type(mylist))
