my_list = [1, 2, 3]

print(f"The amount of items in this list object is: {len(my_list)} items.")

print("===============================")
for item in my_list:
    print("Number: " + str(item))
    print(f"number: {item}")

print("===============================")
mylist = ['one', 'two', 'three']
print(mylist[0])

print("===============================")
print(mylist[1:])
print(type(mylist[1:]))

print("===============================")
another_list = ['four', 'five', 'six']
new_list = mylist + another_list
print(new_list)

print("===============================")
new_list[0] = 'ONE ALL CAPS'
new_list.append('seven')
print(new_list)

print("===============================")
popped_item = new_list.pop() # If using the pop() function without passing an index, it will remove the last item
print(new_list)
print(f"The item removed was: {popped_item}")

print("===============================")
new_list = ['a', 'e', 'x', 'i', 'b', 'c']
num_list = [4,1,8,3]

new_list.sort()
print(new_list)

num_list.sort()
print(num_list)

print("===============================")
num_list.reverse()
print(f"Reversed list {num_list}")