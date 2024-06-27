'''
This solution is slightly faster than the first solution because we do not need to search an array of characters to find
if a char is an open or close paranthesis.  In this solution we use a map so we can do that lookup in constant time

Further, the code is a bit more consise because we condense our if statements in two places:
1. we use if list to check if the list has any contents and then we use list[-1] to get the last element in the array
2. We add a condition to the return statement instead of before the return statemetn to check if the stack has any 
remaining items
'''

class Solution:
    def isValid(self, s: str) -> bool:
        close_map = {'}':'{', ')':'(', ']':'['}
        stack = []

        for c in s:
            if c in close_map:
                if stack and stack[-1] == close_map[c]:
                    stack.pop()
                else:
                    return False      
            else:
                stack.append(c)
            
        return True if not stack else False