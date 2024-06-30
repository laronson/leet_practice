'''
In this problem, we are given a list of integers.  Each index in the integer represents a pile of bananas.  All of the
bananas in every pile must be eating within h (also passed in) hours.  We can set the eating rate at k for how many
bananas we eat per hour.  If a pile has less than k bananas in it, we can finish the pile but we cannot eat bananas from
another pile.  We must return the minimum value k to eat all the banananas in h hours.

To do this, we first must figure out that the max k we can choose is the number of bananas in the largest pile.  This is
because, if we choose this value, we can eat one pile of bananas every hour.  However, this does not mean it will be the
minimum.  From there, we can do a binary search on all the values for k  from 1 - max(piles) to get the minimum value of
k to finish every banana in under h hours.  When searching, we can check our current "mid" value to see if that value of
k gets us a finish time above or below k.  If we are above k, we need to increase our rate of eating up to lower the number
of hours it takes down below h.  However, if we are below h, we decrease our rate of eating and see if that value keeps
us below h.  

One thing to note here, when searching for our k value, we must store the k value at each iteration of our search so we
can store the most recent value before increasing or decreasing or min or max to retain the value from the previous iteration.
'''

import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def numberOfHours(k:int)->int:
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            return hours

        min_k, max_k = 1, max(piles)
        ans = max_k
        while min_k <= max_k:
            # In python this is fine because python integers are unbounded and can be infinately large, however, in
            # other languages that bound ints to be 32 bytes, if max and min are above the max int value, then you may
            # get an overflow error.  Therefore, in other languages, you would need to use (min + (max-min)//2)
            mid =(max_k + min_k)//2

            if numberOfHours(mid) <= h:
                ans = mid
                max_k = mid -1
            else:
                min_k = mid +1

        return ans