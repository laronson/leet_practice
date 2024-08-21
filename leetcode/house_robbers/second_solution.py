'''
This problem presents us with a list of integers that represent a line of houses in a row.  Each house contains a value 
(positive int) that represents the value that can be robbed from that house.  The problem asks us to rob the max amount 
of money from all of the houses but we cannot rob two houses that are adjacent to each other.

To solve this problem, we must first determine how we are going to choose which path to take (from any house) to provide 
us with a path that allows us to rob the max value hoses and still abide by the “no adjacent houses” rule.  The way we 
can do that is by observing each house and determining, at that house, what the max value we can achieve is by the time 
we reach that house.  However, that does not necessarily mean that we are calculating that houses path, it may be the 
case that the max value we can achieve by the time we hit that house is by taking the path which allows us to get to the 
house before it.  Therefore, in order to solve this problem, we can traverse through the list of houses keeping track of 
the max value we can get by the time we reach that house which is either the path the current house is on plus the 
current houses value OR the path of the house that is behind the house we are observing.  

One way you can achieve the strategy described above is by keeping a list of the max values we can achieve at each house 
as we iterate through the list of houses.  However, we will only ever need access to the houses one house back and two 
houses back from our current location (aka the house that the current house would be the next house on that path OR the 
path the previous house is on).  Therefore, we do not need to store a list BUT we only need to store the max values of 
the last two houses as we iterate through our list of houses.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
      rob1,rob2= 0,0
      for houseIdx in range(len(nums)):
        newRobVal = max(rob2+nums[houseIdx], rob1)
        rob2 = rob1
        rob1=newRobVal
      
      return rob1
        