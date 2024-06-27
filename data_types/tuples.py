#TUPLES
# A tuple is a a sequence data type that, unlike the list data type, are immutable, and usually contain a list of 
# items that of different data types.  In most cases, tuples are accessed via unpacking (like spreading in javascript)
#When accessed via the console, tuples will be wrapped in parenthesis.
#Tuples can be nested

#Creating a tuple with tuple packing:
t = 1234, 4567, 'hello'

#Unpacking a tuple
a,b,c = t

#Nested tuples
u = t,(1,2,3)
print(u) #-> ((1234, 4567, 'hello'),(1,2,3))

#tuple with no item.  Note that it is created with an empty set of parenthesis
empty_tuple = ()

#Tuple with single item.  Notice the initiation of a tuple with a single item is created with a trailing comma
single_tuple = 'singleItem',