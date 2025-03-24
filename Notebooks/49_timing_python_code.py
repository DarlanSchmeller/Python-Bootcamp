import time

# CURRENT TIME BEFORE
start_time = time.time()

# RUN CODE

def func_one(n):
    return [str(num) for num in range(n)]

print(func_one(100))


def func_two(n):
    return list(map(str, range(n)))

print(func_two(100))

# GET CURRENT TIME
ending_time = time.time()

# ELAPSED TIME / DIFFERENCE
elapsed_time = ending_time - start_time
print(elapsed_time)

print('----------------------------------')

# Using Timeit module to measure which code is more efficient

import timeit


statement = """
func_one(100)
"""

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

print("Func one:", timeit.timeit(statement, setup, number=100000))

statement_2 = """
func_two(100)
"""

setup_2 = '''
def func_two(n):
    return list(map(str, range(n)))
'''

print("Func_two: ", timeit.timeit(statement, setup, number=100000))
