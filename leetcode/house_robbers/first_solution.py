'''
** This solution works but we can refactor this to avoid needing to store the memo list **
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
      if len(nums)==1:
        return nums[0]
        
      memo = [-1]*len(nums)
      memo[0] = nums[0]
      memo[1] = max(nums[0],nums[1])

      for houseIdx in range(2,len(nums)):
        memo[houseIdx] = max(memo[houseIdx-2]+nums[houseIdx], memo[houseIdx-1])
      
      return max(memo[-1],memo[-2])