### Syntax for Classes

class NameOfClass():

    def __init__(self, param1, param2):     # Allows us to create an instance of our Object/Class
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        # Perform some action
        print(self.param1)

    ## In short everything that has the keyword self, means it's connected to the class INSTANCE (exclusive to the instance created not the whole class)



# _________________________________________________________________

class Sample():
    pass

my_sample = Sample()
print(type(my_sample))

# _________________________________________________________________
class Dog():
    
    # Class Object Attribute
    # THESE ARE THE SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'



    # The __init__ method always gets executed when the class is Instanced
    def __init__(self, breed, name, spots):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name

        # We expect a boolean True/False
        self.spots = spots


        print("Roof")
        pass




my_dog = Dog(breed='Lab', name='John', spots=True)
# my_dog = Dog('Lab', 'John', True) ### This is the same as the above, except the above uses keyword arguments rather than positional
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)

# CALLING A GLOBAL CLASS ATTRIBUTE (same for every class regardless of instance parameters)
print(my_dog.species)