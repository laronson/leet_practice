'''
This solution gets the right answer but runs too slowly.  This solution runs in O(n**2) time because of the way the 
inner while loop is set up to run 
'''

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        
        longest_seq = 0
        for n in num_set:
            next_num = n + 1
            seq=1
            while next_num in num_set:
                seq += 1
                next_num += 1
            longest_seq = max(longest_seq, seq)

        return longest_seq