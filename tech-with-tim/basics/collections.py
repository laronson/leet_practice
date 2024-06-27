#Lists

#Lists are mutable zero indexed ordered collections
x=[4,True,'Hi']
x.append('hello') #Add one element to a list
x.extend([1,3,4]) #Like the spread operator to add the contents of one list to another
popped = x.pop() #Get last item in list
poppedFirst = x.pop(0)
print(len(x))
print(x[0])

#Copies the reference to the array instead of making a copy of the contents of the array
y=x

###
#Tuples
###

#Tuples are immutable lists of items
t = (0,1,2,3)
print(t[0]) #Can access the tuple
#t.append(1) -> Cannot append or change the tuple because it is immutable

#unpacking tuples
t, s = (1,2)