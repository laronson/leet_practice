#unordered set of unique items that has a quick lookup time

s = set()
the_set_literal = {1,2,3,3} #This is just a dict 

s.add(45)
s.remove(45)
print(45 in s)
print(33 in s)

print(34 in s) #constant time
print(34 in [1,3,4,5,6])#linear

print(s.union(the_set_literal))
print(s.intersection(the_set_literal))

