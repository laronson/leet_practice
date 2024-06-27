# Dictionaries are like object types in javascript.  They are essentially a hashmap type that contains a list of key
# value pairs

#Create a normal dictionary type
from collections import defaultdict


dictionary = {'key': 1} 
anotherDictionary = dict()

#Create a dictionary with a default value of an empty list.  NOTE*** the value passed to a defaultdict must be a "callable"
# argument and cannot be a scalar
defaultDictionary = defaultdict(list)

#get a value by key from a dictionary
x = dictionary['key2']
#The above statement will throw a value because 'key' does not exist in dictionary.  We can use the .get() function
#of a dictionary to also set a default return type if the value does not exist
x = dictionary.get('key2', 0)

#Get the key value pairs of a dictionary
dictionary.items()
