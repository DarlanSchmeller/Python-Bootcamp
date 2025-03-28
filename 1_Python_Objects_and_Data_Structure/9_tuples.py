t = (1,2,3)
my_list = [1,2,3]

print(type(t))
print(t[0])
print(t[1])

print('------------------------------')
t = ('a', 'a', 'b')
print(t.count('b')) # How many occurrences of the argument provided
print(t.index('b')) # List index of first occurence of the argument

print('------------------------------')
my_list[0] = "New Item"
print(my_list)
try:
    t[1] = 'Attempt to Add new item'
except Exception as e:
    print(f'Cant modify tuple: {e}')
print(t)