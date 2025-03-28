print(' This is a string: {}'.format('INSERTED')) # Simple method to insert a string into another string
print(' That {} {} {}'.format('dog','is','cute'))
print(' That {0} {0} {0}'.format('dog','is','cute'))
print(' That {d} {i} {c}'.format(d = 'cow', i = 'is', c ='big'))


# Float Formatting

result = 100/77
print(result)

# Float Formatting Syntax: {value:width.precision f}
# Value is the data to be manipulated, width is the required size of the value, and precision is the number of decimal places

print("The result was {r:1.3f}".format(r = result))

result = f"{result:1.3f}" # Another way to do this directly on the variable
print(result)
print(type(result))
print(type(float(result)))


float_value = 10240.42040240
float_value = f"{float_value:1.1f}"

print(float_value)

# f strings are used to insert variables into strings in a simpler way, the syntax is f"string {variable}", it's much simpler than .format