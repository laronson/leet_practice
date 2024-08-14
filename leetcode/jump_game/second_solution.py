'''
This problem presents us with a list of jump lengths.  Each jump length represents the max number of spaces we can jump 
from our current space.  For example, if we are at index 0 and jumps[0] == 3, that means we can jump to index 1,2 or 3 
from our current location of index 0.  The problem asks us to return a boolean that represents whether or not we can 
make it from index 0 to the final space within the list (aka len(jumps)-1).

To solve this problem, we can think about the jumping mechanic incrementally working backwards from the end of the list.  
To get to the goal of the end of the list, a space must exist before that space where idx+jump[idx]==goal.  Therefore, 
we can iterate backwards from the end of the list (starting at the second to last index of the list) and iterate until 
we find a space where we can jump from to reach the goal.  If we hit that space, we reset our goal to be that space and 
then start searching for a space from where we can jump to our new goal.  We continue this process until we hit the end
of the list.  At that point, if our goal has been reset to 0, then it means that our starting point at index 0 can reach 
the goal (which may lead us to secondary goals from where we can reach the end).  Therefore, we can return a conditional 
that checks if our goal has been set to 0 after iterating through the entire list.  If goal == 0, then we can reach the 
end, otherwise we cannot.
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
      goal = len(nums)-1

      for idx in range(len(nums)-2,-1,-1):
        if (idx+nums[idx]) >= goal:
          goal = idx
      return goal==0