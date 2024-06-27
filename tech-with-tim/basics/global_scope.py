'''
Global variables does not work the same way that it does in javascript.  If a vairable is global and you try to change 
it from a function within the same file, the function does not actually change the value of the global
'''

x = 'tim'

def no_change(change_to):
    x = change_to

def does_change_never_do(change):
    global x #NEVER DO THIS!!!
    x=change

print(x)
no_change("CJHANGE")
print(x) #Still Tim
does_change_never_do("CHANGE")
print(x) #Changed from tim