class Dog:
    #Instantiating variables before init is where you would put static variables that do not need to be initialized
    #inside of the __init__ method.  These variables also belong to the class AND NOT the indevidual instances of the 
    #class.  Therefore, when we append the dogs list in the init function, if we were to reference this variable in any
    # instance of the class, it would represent the same value
    dogs = []
    has_ears = True

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)
    
    @classmethod #this is a decorator to tell python that this is a special type of method
    def num_dogs(cls):
        #The cls variable allows us to reference the class itself 
        return len(cls.dogs)
    
    @staticmethod
    def bark(n):
        for _ in range(n):
            print("Bark")

tim = Dog("Tim")
isla = Dog("Isla")

#You do not need to reference class variables or class methods on an instance of the class
print(Dog.dogs)
print(Dog.num_dogs())

# Static methods are allowed to be called off of a class but static methods do not have any reference to the class or 
# any instances of the class.  Static methods are good when you want to organize methods inside of a class but do not 
# want to have that class need to be instantiatable.  A good use case for static methods on a class would be the math 
# package.
Dog.bark(3)



