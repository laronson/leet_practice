class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def change_age(self, age):
        self.age=age

    def talk(self):
        print('Bark!')

    def speak(self):
        print(f'my name is {self.name} and my age is {self.age}')

#Cat inherits the class attirbutes of Dog.
class Cat(Dog):
    def __init__(self,name,age,color):
        super.__init__(name,age) #calling init on the superclass
        self.color = color
        self.name = 'new name' #overriding the instance method created in super

    #Overriding the talk method from the inherited dog class
    def talk(self):
        print('Meow!')

bingo = Cat("bingo", 4, 'black')
bingo.speak()
bingo.talk() #meows instead of barks