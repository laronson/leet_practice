def func(x): 
    def func2():
        print(x)
    return func2

print(func(3)()) #Print output if func to be none but then print output of returned func2 to be 3

x=func(45)
x() #prints bound value of 45 

###
# *args, **kwargs
###

arr=[1,2,3,4,5,6]
print(*arr) #Unpack all of the elements of x

def funcxy(x,y):
    print(x,y)

pairs = [(1,2),(3,4)]
for pair in pairs:
    funcxy(pair[0], pair[1]) #NOOOOOO 
    funcxy(*pair) #Can unpack using the * operator

#Can do with dictionary too
funcxy(**{'x':1,'y':2})

#Can use *args and **kwargs as function parameters 
def funcAllTheParams(*args,**kwarsgs):
    print(args,kwarsgs)

funcAllTheParams(1,2,3,4,5,one=0,two=1)

