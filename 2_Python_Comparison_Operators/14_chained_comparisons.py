print(1 < 2 and 2 < 3)
print('h' == 'h' and 2 == 2)

print(100 == 1 or 2 == 2) # Returns True as long as one condition is true

my_list = [4,3,2,1]
my_dictionary = {'k4' : 4, 'k3' : 3, 'k2' : 2}

if 5 not in my_list:
    print('5 is not in my_list')

if 2 not in my_dictionary.values():
    print("Couldn't find 2 in the my_dictionary.")
elif 2 in my_dictionary.values():
    print("Found 2 in the my_dictionary.")


print(not 1 == 1) # Returns the opposite value of the condition