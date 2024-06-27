#Lambdas are one line anonymous functions

x = lambda x, y: x + y #Same as (x,y)=>x+y

print(x(1,2))

x = [1,23,3,4,5,6,3,3,45,5,34,1,45,56,6,6,45,4]
mp = map(lambda item: item+2, x) #returns a map object
print(list(mp))
filtered_list = filter(lambda item: item<45, x)
print(list(filtered_list))

def filterFunc(item):
    return item < 45
filter_with_function = filter(filterFunc, x)
print(list(filter_with_function))