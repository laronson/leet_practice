import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self,x,y):
        self.x += x
        self.y += y

    #def length(self):
    def __len__(self):
        return math.sqrt(self.x**2 + self.y**2)

    # This overrides the + arithmetic operator so we can add two point classes together 
    def __add__(self,p):
        return Point(self.x + p.x, self.y + p.y)
    
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)
    
    def __mul__(self, p):
        return self.x * p.x, self.y * p.y # does not return a new point object
    
    #greater than
    def __gt__(self, p):
        return self.__len__() > p.__len__()

    #greater than or equal to
    def __ge__(self, p):
        return self.__len__() >= p.__len__()

    #greater than or equal to
    def __lt__(self, p):
        return self.__len__() < p.__len__()

    #greater than or equal to
    def __le__(self, p):
        return self.__len__() <= p.__len__()

    #equal to
    def __eq__(self, p):
        return self.x == p.x and self.y == p.y
    
    #Tells python how to print out the string (like .toString())
    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1,2)
p2 = Point(3,4)
#len(p2)

#p1 becomes self in the __add__ method and p2 becomes the pass p Point object 
p3 = p1 + p2 # returns a new point at (3,6)
p4 = p1 - p2
p5 = p1 * p2

print(p3, p4, p5)

print(p1 == p2)
print(p1 < p2)
