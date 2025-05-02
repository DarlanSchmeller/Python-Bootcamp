d = {'k1':1,'k2':2}

# There is dictionary comprehension that is similar to list comprehension but not very common
print({x:x**2 for x in range(10)})
print({k:v**2 for k,v in zip(['a','b'], range(2))})

for k in d.values():
    print(k)

print(d.items())