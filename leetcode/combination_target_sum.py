'''
This problem presents us with a list of numbers and a target.  We are asked to find all combinations of numbers in the 
nums list that add up to target.  We are allowed to use each number in the nums list as many times as we want.  Each 
list in the result must be distinct.

To solve this problem, we first must think about how we construct an aggregate list.  When looking at each number in the 
nums list, we have a choice of whether to add that number to our sum or not.  Therefore, each aggregate list is made of 
a decision chain of whether or not we add a number from the nums list X number of times.  To generate the list of 
aggregate lists, we can use a recursive dfs traversal of the nums list where, for each recursive call we inspect each 
number in the list X number of times and we decide to add it to the aggregate array or not.  If we end up with an 
aggregate that is equal to target, we save that aggregate list.  If the aggregate is less, we continue to add the same 
number over and over again.  Once we exceed or equal target, we remove the last value in the list and start adding the 
next number X number of times.
'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, agg, aggSum):
          if idx > len(nums)-1 or aggSum > target:
            return
          if aggSum == target:
            res.append(agg.copy())
            return

          agg.append(nums[idx])
          dfs(idx, agg, aggSum + nums[idx])

          agg.pop()
          dfs(idx + 1, agg, aggSum)
        
        dfs(0, [], 0)
        return res