my_list = [1, 2, 3]

print(len(my_list))

class Sample():
    pass

my_sample = Sample()
### Generates Type Error because Class has no Length
# print(len(my_sample))

print('---------------------')
##############################

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    ### The __str__ Method it's a special method that defines a string representation of an object
    # since by default, if you don't define a __str__ method, Python shows the class name and memory address, 
    # overriding __str__ allows to  customize the string representation when printing or converting the object.
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    # We can do the same for Length
    def __len__(self):
        return self.pages
    
    # We can also define a custom behavior
    # for deleting instances of our class
    def __del__(self):
        print('A book object has been deleted')


book_one = Book(title='Python Rocks!', author='Darlan', pages=324)
### This attempts to convert the class to a String
# Which is why we get the location in memory when attempting to print it
# That is unless we use the special __str__ method
print(book_one)
print(len(book_one))

# Allows us to delete the instance from Memory
del(book_one)
# This may also be redefined with the __del__ method