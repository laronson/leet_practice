hello = 'hello'.upper()
print(hello)

hello2='HELELO'.lower()
print(hello2)

hello3 = 'hELLO WORLD'
print(hello3.capitalize()) #Capitalize the first letter of the string and then lower case for the rest 

hello4 = 'hello world'
print(hello4.count('ll')) # Look for the number of times a substring appears in the parent string


hello5 = "COPY ME"
print(hello5*5) #Copies string 5 times

#Get the ordinal (ASCII) code of a character
print(ord('a'))#->97