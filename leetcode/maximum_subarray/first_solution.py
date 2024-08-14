'''
** This solution works but can be refactored to be cleaner **
nums -> List[int]
find subarray with the largest sum

[-3,1,2,-4,2,2,-5] -> 4
[1,2,3,4] -> 10
[-1,-2,-3] -> -1

1. init left and right pointer to be at index 0
2. move r to the right keeping track of sum along the way
3. Once hit a number that decreases the sum, snake left while the sum increases
4. Keep track of max sum through all moves of 2 and 3
'''

#[-3,1,2,-4,2,2,-5]
#        lr
#runningSum = -4
#maxSum = -4
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      if len(nums) == 1:
        return nums[0]
      
      l, r = 0, 1
      runningSum = maxSum = nums[l]

      while r<len(nums):
        runningSum+=nums[r]
        if (runningSum) <=0:
          l = r
          runningSum = nums[l]

        while (runningSum - nums[l]) > runningSum and l<r:
          runningSum-=nums[l]
          l+=1
        
        maxSum = max(runningSum,maxSum)
        r+=1
      return maxSum
        

      return maxSum

        