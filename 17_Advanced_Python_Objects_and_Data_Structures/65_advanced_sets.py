s = set()

s.add(1)    # Add an element to a set.
s.add(2)
print(s)

s.add(2)

s = {1,2,3}
sc = s.copy()   # Return a shallow copy of a set.
print(sc)

s.add(4)
print(sc)

print(s.difference(sc))     # Return the difference of two or more sets as a new set.

s1 = {1,2,3}
s2 = {1,4,5}

s1.difference_update(s2)    # Remove all elements of another set from this set.
print(s1)

s.discard(12)   # Remove an element from a set if it is a member.
print(s)

s1 = {1,2,3}
s2 = {1,2,4}
print(s1.intersection(s2))      # Return the intersection of two sets as a new set.

s1.intersection_update(s2)      # Update a set with the intersection of itself and another
print(s1)

s1 = {1,2}
s1 = {1,2,4}
s3 = {5}

print(s1.isdisjoint(s2))    # Return True if two sets have a null intersection
print(s1.isdisjoint(s3))

s1.issubset(s2)     # Report whether another set contains this set.

s2.issuperset(s1)   # Report whether this set contains another set.

