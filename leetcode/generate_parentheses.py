'''
The general idea behind this solution is to backtrack for every combination of starting paranthesis and add in the end
parenthesis.  The two things to note about this solution is the following:
1) The backtracking solution is instantiated within the main function itself.  This gives the benefit of allowing us
to use "global" variables when recursing through the backtracking functions
2) After we return from a call to backtracking we need to remove the change to the array string that we made when entering
into the backtracking solution.  This is because we need to allow the solution to attempt to add both open and close
parenthesis for every valid starting combination
'''
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []

        def backtrack(open_p, closed_p):
            if open_p == closed_p == n:
                ans.append(''.join(stack))
                return

            if open_p < n:
                stack.append('(')     
                backtrack(open_p+1, closed_p) 
                stack.pop()
                
            if closed_p < open_p:
                stack.append(')')
                backtrack(open_p, closed_p+1)  
                stack.pop()
    
        backtrack(0,0)

        return ans