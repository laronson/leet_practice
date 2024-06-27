#in order to arithmatic operators to work, the data type on both the left and right side of the operations must be the 
#same

x=9
y=3
result = x+y
print(result)

result = x-y
print(result)

result = x*y
print(result)

result = x/y
print(result)
#Devision always returns a floating point number
#can convert to int by using the int data type conversion 
result = int(x/y)
print(result)

#Raise to the power to
result = x ** y
print(result)

#Floor division - automatically takes the .floor() of the division result 
result = x // y
print(result)

#mod
result = x%y
print(result)


#taking a number inpuit from the user takes an input number as a string.  Therefore we need to convert that number into 
# an integer first
num = input('Number: ')
print(int(num)-5)
print(float(num)- 5)