
#Class dog that extends object
class Dog(object):
    #The constructor method of the class
    #the self keyword is like the this keyword in JS and allows an instance of an object to reference itself 
    def __init__(self, name, age):
        print("there is a new Dog")
        self.name = name
        self.age = age
        self.internal_list = [1,23,3,45]
    
    def change_age(self, age):
        self.age=age
        #pass if you dont have anything in your function you can use the pass keyword
    
    def add_weight(weight):
        self.weight = weight #Despite the warning you can do this but it basically eliminates type safety

    def speak(self):
        print(f'my name is {self.name} and my age is {self.age}')

isla = Dog('Isla', 3) #instance of type dog
otis = Dog('Otis', 13)
isla.speak()
otis.speak()
isla.change_age(3.5)
isla.speak()

#You can directly access the attributes of an object
print(isla.age)
print(isla.internal_list)