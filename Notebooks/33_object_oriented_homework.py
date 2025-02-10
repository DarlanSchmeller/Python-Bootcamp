### Object Oriented Programming
### Homework Assignment

# #### Problem 1
# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
# # EXAMPLE OUTPUT
# coordinate1 = (3,2)
# coordinate2 = (8,10)
# li.distance() : 9.433981132056603
# li.slope() : 1.6

class Line:
    def __init__(self,coor1,coor2):
        self.coor_x1, self.coor_y1 = coor1
        self.coor_x2, self.coor_y2 = coor2

    def distance(self):
        return ( ((self.coor_x1 - self.coor_x2)**2) + ((self.coor_y1 - self.coor_y2)**2) ) ** 0.5
    
    def slope(self):
        return (self.coor_y2 - self.coor_y1) / (self.coor_x2 - self.coor_x1)
    
my_line = Line((3,2), (8,10))
print(my_line.distance())
print(my_line.slope())

# __________________________________________________________________________________________________________________________
# #### Problem 2
# Fill in the class 
# # EXAMPLE OUTPUT
# c = Cylinder(2,3)
# c.volume() : 56.52
# c.surface_area() : 94.2

class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return 3.14 * (self.radius**2) * self.height
    
    def surface_area(self):
        return (2 * 3.14) * self.radius * (self.radius + self.height)

my_cylinder = Cylinder(2, 3)
print(my_cylinder.volume())
print(my_cylinder.surface_area())