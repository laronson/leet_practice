###
# for loops
###

#The range function is used to set the bounds of the loop that creates a collection of numbers based on the input
#The inputs are range(start,stop,step) like a for loop in js but just in the range function
#range(10) -> this is actually range(stop) range(10,11) -> range(start,stop) range(10,1,-1) -> range(start, stop step)
for i in range(10):
    print(i)

#Print through in a range
for i in [1,3,5,76,4,2]:
    print(i)

#loop through the values of an array and also gain access to the index
arr = [1,3,5,76,4,2]
for i, element in enumerate(arr):
    print(i, element)

###
#while loops
###

while True:
    print("running")
    break