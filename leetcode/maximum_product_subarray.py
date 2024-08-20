'''
nums -> integer array
return: integer -> the product of a subarray within nums that has the largest product of all values
  in that subarrry

Rules:
  - len(nums) 1 - 1000
  - values in nums can be between -10 and 10
  - product is reasonable to fit in a 32 bit number
  - A single value would be an implied *1

[-1 2 3 4] 24
1 12 123 1234 2 23 234 3 34 4
[1 2 3 -4] 6
[1 0 0 4] 4

growing product is increasingly positivie numbers 
OR
increasiongly positive numbers with a mix of an even count of negetive values

[1 100 -3 10]
n -3
tmp -300
max -3
min -300
res 100
'''

'''
This problem presents us with a list of integers and asks us to find the subarray within that list which contains 
numbers that produce the maximum product among all other possible subarrays.

At first glance, we could decide to use a brute force algorithm and calculate the product of every subarray using a 
recursive or iterative approach.  This would result in an O(n!) runtime.  However, we can use dynamic programming to 
solve this problem in O(n) time.  To do this, we must realize that, for every value in the list, we can calculate the 
minimum and maximum product we can make using (or leaving out) all of number before it.  If we store that information, 
when looking at the next number, we can determine how that next number would affect the minimum and maximum values we 
have pre-calculated which would in turn give us the minimum and maximum product we can make at that number.  Using this 
strategy, we can iterate through our list of numbers keeping track of the min and max subarray product values we can 
make at each index.  As we do this, we can use a result variable to keep track of the max value we see throughout our 
iteration and return that value at the end of our iteration to return the max product.
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
      res = nums[0]
      currMin, currMax = 1,1

      for n in nums:
        tmp = n * currMax
        currMax = max(n*currMax, n*currMin, n)
        currMin = min(n*currMin, tmp, n)
        res = max(res,currMax)
      return res
      
        