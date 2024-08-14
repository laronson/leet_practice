'''
nums: List[int] -> nums[i] indicates how many spaces you can jump from index i
output: boolean -> if you can reach the last index in the list from index 0

len(nums) == 5 -> 4
no negetive numbers

[1,2,1,0,1]
[1,2,0,1,0]
idx=4
longest=4 
maxLongest =4 

'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
      longest,maxLongest = 0,0

      for idx in range(len(nums)):
        longest = (idx+nums[idx])
        maxLongest = max(maxLongest,longest)

        if idx >= maxLongest and idx!= (len(nums)-1):
          return False
      

      return True
        