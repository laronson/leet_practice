'''
This problem presents us with a list of integers nums and asks us to find to numbers i, and j that represent indices 
within nums where i < j and nums[i] ≤ nums[j].  Of the valid combinations of i and j that meet that criteria, we are 
asked to find the combination of i and j that maximizes the difference between i and j and return the difference.

At first glance, the brute force solution for this problem would be to loop through every pair of i and j values, find 
all pairs that meet the criteria, keeping track of the max difference value we see throughout our iteration.  This 
solution would run in O(n^2) runtime but we can probably do better.  However, from this exercise we can glean that a two 
pointer approach could be a decent strategy for finding our pair of i and j. 

If it is the case that we are trying to find the largest difference between i and j that meets the criteria, the largest 
value we can possibly get is when i=0 and j=len(nums).  Because it is the case, we could use a two pointer approach 
where i and j start in those positions and then move our pointers inward (like the water tank question).  However, 
because our list is not sorted, it is possible that moving our right pointer to the left or left pointer to the right 
when that criteria is not met could make us miss the optimal solution.  There is no concrete rule that would allow us to 
base our movement decisions on just the two values at i and j.  Because of our inability to determine which value to 
move, we should rethink our two pointer strategy.

At this point, it would be worth thinking about another one of our two-pointer strategies, sliding window.  If we use 
this approach, we can start our i and j pointers at index 0 and 1 respectively, and we move both i and j to the right.  
However, how do we know if we should move i or j?  Thinking about the two types of movement individually, we would want 
to move j if we know that moving j would continue to increase the size of our difference and that movement would 
continue to keep i and j meeting the criteria.  But when do we want to move i to the right?  We would want to move i to 
the right if the value at i is less than the max value we have seen (coming from the left) up until the location of 
index j:

nums= [6,0,8,2,1,5] - increase j until j is at index 3 because the max val at that point is 5
maxs= [8,8,8,5,5,5]

Once the max value we have seen at j is less than the value at i, we must move i to the right until that value at i is 
less than the max_value we have seen at j.  At that point, we can calculate the distance between i and j because we know 
that at any value between i and j, i will always be greater than the value at j because the max value we have seen 
coming from the right up until that point is less than the value at i.

To apply this strategy, we must first run through nums from the right and for each index in nums, we store (in a new 
list) the max value we have seen coming from the right up until that point.  Once we have those values, we initilize our 
two pointers i and j to be 0 and 1 respectively.  We loop through a list from j=1 to j=len(nums) to move j to the right.  
If at any point during our iteration of j, we see that the value at i is greater than the max value we have seen coming 
from the right at index j, we increase i until that is not the case.  Once i have been move to a valid spot, we 
calculate the distance between i and j, keep track of the max distance we have seen, and once we complete our iterations 
of j, we return our max distance.
'''

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_seen = [0]*len(nums)

        prev_max,i = nums[-1], len(nums)-1
        for n in reversed(nums):
            if n >= prev_max:
                prev_max = n
            max_seen[i]=prev_max
            i-=1
        
        l = res = 0
        for r in range(1,len(nums)):
            while nums[l] > max_seen[r]:
                l+=1
            res = max(res,r-l)
        return res