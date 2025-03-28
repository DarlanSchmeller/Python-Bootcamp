# Import Python Debugger
import pdb

x = [1,2,3]
y = 2
z = 3


result = y + z

# When set_trace() is hit during execution, it pauses the program at that line, allowing you to step through the code, verify variables, run operations and check how the data is being managed.
pdb.set_trace()
result2 = x + y