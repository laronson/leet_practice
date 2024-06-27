'''
This solution fails when there are negetive numbers in the mix.  This is because when there are only positive numbers 
present, python will print the set's values in order.  For set([5,4,3,2,1]), the set will print as {1,2,3,4,5}. However
for set([1,0,-1]), the set will print as {0,1,-1}.  Because of this, sets with only positive numbers will work because
the algo will search for sequences starting with the smallest number.  However, when negetive numbers are present, those
numbers get searched for after positives making the rest of the solution not work as intended.
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        visited_set = set()
        print(num_set)
        
        longest_seq = 0
        for n in num_set:
            next_num = n + 1
            seq=1
            while next_num in num_set and next_num not in visited_set:
                visited_set.add(next_num)
                seq += 1
                next_num += 1
            longest_seq = max(longest_seq, seq)

        return longest_seq