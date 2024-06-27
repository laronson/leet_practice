'''
This was a problem that started to re-use past strategies with a twist.  In this problem I was tasked to find sets of
three numbers in an array that summed to 0 without adding duplicates to the array.  To do this, the strategy was to
first sort the array so we could take advantage of the two-pointer strategy we used in the two-sum problem.  Once sorted
we could iterate through the array and then to the right of our current index, use the two pointer strategy to find
two numbers that, with our current index, added to zero.  There were a few things to consider here:
1) we needed to be careful that we did not add any duplicate sets to our ans array.  Therefore, we needed to keep a second
set to keep track of values that we used as our set value (the value at the index in the top iterator).  That way, if 
there was a duplicate value in the array base array that we already calculated sets from, we would not do it again.
2) Because there could be multiple combinations of sets for a given start value, we needed to continue to iterate
through the entire right side of the array even if we hit a valid set.  To do this, if we found a set, we added the set
to ans and then moved the left and right pointers and started our search again.  HOWEVER, we needed to be careful that 
the value at the left idx did not equal the value we previously used at left because that would also cause us to add a
duplicate set.  Therefore we needed to add another loop to iterate left as many times as nessisary until we hit a new
value AND left was still less than right.

This was a edge case powerhouse question.  Make sure to not miss edge cases by asking questions like, what combos would
cause a duplicate to occur?  With array questions, make sure that you dont just think of array length edge cases but also
array values edge cases.
'''

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        seen = set()

        idx = 0
        while nums[idx] <= 0 and idx < len(nums)-1:
            if nums[idx] not in seen:
                compare, start, end = nums[idx], idx+1, len(nums)-1
                while start < end:
                    if (nums[start] + nums[end] + compare) < 0:
                        start += 1
                    elif (nums[start] + nums[end] + compare) > 0:
                        end -= 1
                    else: 
                        ans.append([nums[start], nums[end], compare])
                        # push left and right towards each other as we know that only pushing one will not result in
                        # a valid threesome and we might as well push both.
                        start+=1
                        end -= 1
                        #Make sure to continue to iterate left if the value we are now pointing to is the same as the 
                        #last value.  CAREFULE THOUGH make sure to still add the condition that start < end here so we
                        #dont try to access values at indexes that do not exist in our array.
                        while nums[start] == nums[start-1] and start < end:
                            start+=1

            seen.add(nums[idx])
            idx += 1

        return ans
