'''
This solution is acceptable, however, we can reduce the code with some better python syntax in order to prevent the need
to write a seperate if statement to check the length of the stack during iteration
'''

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []

        for c in s:
            if c in ['{', '[', '(']:
                bracket_stack.append(c)
            else:
                if(len(bracket_stack) == 0):
                    return False 
                
                top=bracket_stack.pop()
                if(c=='}' and top != '{' 
                    or c==']' and top != '[' 
                    or c==')' and top != '('):
                    return False

        # Remember to check the length of the stack after iteration to make sure there are not any trailing open
        # brackets 
        if(len(bracket_stack) > 0):
            return False
            
        return True
        