a = "Hello World"
b = " it is beautiful outside"

a = a + b
print(a)

b = a.upper()
print(b)

print(b.split())
print(type(b.split()))

print(b.split('O')) # Splits words on the O's

split_variable = b.split()

counter = 0
for b in split_variable:
    counter += 1
    print(f"String {counter}: " + b)