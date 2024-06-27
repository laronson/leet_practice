from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_set = {'+','-','*','/'}
        op_stack = []

        for token in tokens:
            if token not in op_set:
                op_stack.append(int(token))
            else:
                if len(op_stack)>=2:
                    res = self.operate(token, op_stack[-2], op_stack[-1])
                    op_stack=op_stack[:-2]
                    op_stack.append(res)
            print(op_stack)
        
        return op_stack.pop()

    def operate(self,operator:str, v1:int, v2:int):
        if(operator=='+'):
            return v1+v2
        elif (operator=='-'):
            return v1-v2
        elif (operator=='*'):
            return v1*v2
        elif (operator=='/'):
            #I originally tried using floor division here, but that did not work because if one value in the division
            #is negative then the value will round down to the next lowest negetive number trending away from zero.
            #Therefore, we can use the int conversion here to ensure that the rounded value trends twards zero
            return int(v1/v2)