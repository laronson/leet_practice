'''
This solution is a refactor on the first solution to make the runtime complexity O(n) instead of o(n*26).  The runtime
is reduced in this solution because instead of summing all letter counts and finding the max of all letter counts in
each iteration, we just keep track of the max char_count and use the algorithm r-l+1-max_char_count 
(length_of_substring - number of already same characters) to get the number of characters in the substring that we 
would need to change.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r, max_len = 0,0,1
        max_char=1
        char_counts = {}

        while r < len(s):
            c = s[r]
            char_counts[c] = char_counts.get(c,0) + 1 
            max_char = max(max_char, char_counts[c])

            while k < (r-l+1-max_char) and l<=r:
                cl = s[l]
                char_counts[cl] -=1
                max_char = max(max_char, char_counts[cl])
                l+=1
            
            max_len = max(max_len,(r-l+1))
            r+=1

        return max_len

