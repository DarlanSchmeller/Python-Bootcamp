def create_cubes(n):

    for x in range(n):
        yield x**3 # way more efficient memory wise

for x in create_cubes(10):
    print(x)


print("-------------------------")

def gen_fibon(n):
    a = 1
    b = 1

    for i in range(n):
        yield a
        a,b = b, a + b

for number in gen_fibon(10):
    print(number)

print("-------------------------")
def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

print("-------------------------")
# This is what default Python generators do:
g = simple_gen()
print(next(g))
print(next(g))
print(next(g))

print("-------------------------")
s = 'Hello'
for letter in s:
    print(letter)
print("--")

# next(s)     # Generates 'S' is not an interator error
s_iter = iter(s)     # Iter function converts objects to be iterable
print(next(s_iter))