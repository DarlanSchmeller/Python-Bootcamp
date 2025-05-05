l = [1,2,3]

l.append(4)     # Append object to the end of the list.
print(l.count(1))       # Return number of occurrences of value.


x = [1,2,3]
x.append([4,5])     # Adds the list as a whole to the end of the parent list.
print(x)

x = [1,2,3]
x.extend([4,5])     # Extend list by appending elements from the iterable.
print(x)

l.index(3)        # Return first index of value.
# l.index(10)       # Returns an error if you attempt to find a value not in the list
l.insert(2,'inserted')      # Insert object before index.
print(l)


ele = l.pop()
print(ele)

l.remove('inserted')        # Remove first occurrence of value.
print(l)
l.remove(3)

l.reverse()     # Reverses the list.
print(l)

l.sort()        # Sort the list in ascending order and return None.
print(l)