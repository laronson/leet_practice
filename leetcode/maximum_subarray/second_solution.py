class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      runningSum,maxSum = 0, nums[0]

      for n in nums:
        runningSum+=n
        maxSum = max(maxSum,runningSum)
        if runningSum <0:
          runningSum = 0
          
      return maxSum