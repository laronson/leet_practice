'''
The slice operator has the following format
sliced_array = x[start:stop:step] Like the range function
'''

x=[0,1,2,3,4,5,6,7,8,9]
y=['hi','hello','goodbye','cya','sure']
s='hello'

sliced_stepped_array = x[0:4:2]
sliced_subarray = x[2:4]
sliced_array_to_end = x[3:]
sliced_array_to_middle = x[:4]
reversed_subarray = x[4:2:-1]
reversed_full_array = x[::-1]

reversed_string = s[::-1]

reversed_tuple = (1,2,3,4,5)[::-1]

