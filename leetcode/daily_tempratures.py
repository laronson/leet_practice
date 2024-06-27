'''
To solve this problem, within an array of values, we needed to determine how far away the next higher number was from
each value.  To do this, we could use a stack where we iterated through the original array and only pushed values that 
were lower than the value being stored at the top of the stack.  If we hit a value that was greater than the top of the
stack, we knew that we had hit the next highest value compared to the value at the top of the stack.  Therefore, we could
push the distance from the value at the top of the stack to an answer array.  However, the problem there is how do we
know how far away the top of the stack is from the current value.  In an ideal case, the sequences would be sorted and
the value at the top of the stack would be 1 away and the next value would be two away ect... However, this may not be 
the case in that we may have lower an higher values in the middle of two relatively larger values making it so we cannot
assume that we are always +1 away.  Therefore, instead of storing values on the stack, we stored indexes
that pointed to values in passed array on the stack.  Therefore we can compare the index of the current max value to
the indexes stored in the stack and use those to get the distances between the values.
'''

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        
        ans = [0]*len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while len(stack) > 0 and t > temperatures[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)

        return ans
            
        