'''
In this problem, we are given a list of numbers in asc order that could have been rotated to the right any number of
times.  For example, the array [1,2,3,4,5,6] could be rotated 3 times to be [4,5,6,1,2,3].  For the array that is
passed, return the lowest value in the array.

The problem asks for us for a solution that runs in O(log(n)) time.  Because this is a searching problem, I knew that it
was most likely a binary search problem.  Then applied the BS algo to the array to see to test and see if I could use
the algo even though the list was sorted.  It turns out that if I applied new rules to my pointer rules, I could use BS
to find the lowest value.  I set out new rules which were all defined based off of whether or not the mid value was
greater or less than the right values.  I also kept track of the most min value we saw as we were iterating because, as
we have seen in other problems, If we do not know what we are looking for, we need to keep track of that inside of
another variable.
'''

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0, len(nums)-1
        min_val = nums[0]

        while l <= r:
            mid = (l+r)//2
            min_val = min(min_val, nums[mid])

            if nums[mid] >= r:
                l = mid + 1
            else: 
                r = mid - 1

        return min_val