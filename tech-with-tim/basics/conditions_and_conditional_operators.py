#This runs a comparison letter by letter to see if the letter in spot s2[0]>s2[0] if it is equal, 
#then check the next character s1[1] > s2[1].  Go until there is a potential inequality
print('ab' > 'ad') 

#chained conditionals
# and, or, not
#order of operations is 1)not 2)and 3)or
x=7
y=8
z=0

result1 = x==y
result2 = y>x
result3 = z < x+2

result4 = result1 or not result2 or result3
print(result4)

result5 = result1 and result2

#If/else statements
name = "Tim"

if name == "Tim":
    print("you are Tim")
elif name == "Jim":
    print("Your not Tim you're Jim")
else: 
    print("In the else")

print("This will always run")