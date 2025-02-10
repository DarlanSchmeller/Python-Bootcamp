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
        # Attributes
        # We take in the argument and Assign it using self.attribute_name
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
        print("Dog was Born")
    
    # OPERATIONS/Actions ---> Methods
    def bark(self, number):
        print(f"WOOF WOOF! My Name is {self.name} and the number is {number}")




my_dog = Dog('Lab', 'Frankie')
# my_dog = Dog('Lab', 'John', True) ### This is the same as the above, except the above uses keyword arguments rather than positional
print(my_dog.breed)
print(my_dog.name)
my_dog.bark(4)

# CALLING A GLOBAL CLASS ATTRIBUTE (same for every class regardless of instance parameters)
print(my_dog.species)


class Circle():

    # CLASS OBJECT ATTRIBUTE | Same for every instance
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * self.pi

    def get_circunference(self):
        return self.radius  * self.pi * 2

my_new_circle = Circle(30)
print(my_new_circle.radius)
print(my_new_circle.pi)
print(my_new_circle.area)
print(my_new_circle.get_circunference())


# ----------------------------------------------------------------------
print('-------------------------------')

class Animal():
    
    def __init__(self):
        print("ANIMAL CREATED!")

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

my_animal = Animal()
my_animal.eat()
my_animal.who_am_i()

print('_______')

### DERIVED CLASS
# With Derived Classes we pass a previously created Class when defining it
# This allows us to use previously defined methods and behaviors rather than rewriting
# and having to do all this work again
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    def who_am_i(self):
        print("I am a dog")

    def bark(self):
        print('WOOF WOOF!')

    def eat(self):
        print('I am a dog eating')

my_new_dog = Dog()
my_new_dog.who_am_i()
my_new_dog.bark()
my_new_dog.eat()

print('_______')

### Polymorphism

class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says WOOF!'
    
class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says MEOW!'
    
niko = Dog('Niko')
felix = Cat('Felix')
print(niko.speak())
print(felix.speak())

for pet_class in [niko, felix]:
    print(type(pet_class))
    print(type(pet_class.speak()))


def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)

#============================================
print('_______')

### ABSTRACT CLASS
class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this Abstract Method")
    
my_animal = Animal('Dog') 
### Generates us an error if we attempt to run this line
# my_animal.speak()

class Dog(Animal):
    
    def speak(self):
        return self.name + ' says WOOF!'
    
class Cat(Animal):
    
    def speak(self):
        return self.name + ' says MEOW!'
    
my_other_dog = Dog('Fido')
my_other_cat = Cat('Isis')
print(my_other_dog.speak())
print(my_other_cat.speak())