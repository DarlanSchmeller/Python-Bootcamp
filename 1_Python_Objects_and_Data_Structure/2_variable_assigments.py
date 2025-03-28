a = 5 # Normal Variable Assignment
print (f"Variable A = '{a}'")

b = 45
print (f"Variable B = '{b}'")



c = a + b # Adding two values together to generate a new variable
print (f"Variable C = '{c}'")


print(f"Variable C data type = {type(c)}") # Python Default function to verify the data type

c = 'Hello World' # Python is Dynamic Typed, meaning data types can be changed dynamically
print(f"Variable C = {c}")
print(f"Variable C is now of the data type: {type(c)}")

# ====================================================================================

my_income = 1000

tax_rate = 0.1 

my_taxes = my_income * tax_rate

print(f"My total taxes are {my_taxes}")