'''
Another classic sliding window problem.  In this problem, we are given a string and we are asked to find the longest
substring within this string where letters are not repeated in the substring.  We are asked to return the length of the
longest substring we can find.

To solve this problem, we first need a set to keep track of all of the values in the substring that we are looking at.
With that, we can use a sliding window strategy to trace through the string where both left and right pointer start at
0.  If the value at right does not exist in the seen set, we add that value to the seen set, calculate the length of the
current substring between left and right pointers, and then compare the length to the max length and choose the largest
one so we keep track of the largest substring that we have seen.  If we encounter a letter a right that exists in our
substring, we increase the left value, remove the value from seen at l until the value at the right pointer is removed
from the seen set OR the left and right pointer are at the same place in the string.  Once we have snaked through ever
value (aka the right pointer is at the end of the string), we return the max length that we have found.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = r = 0
        max_len = 0

        while r < len(s):
            if s[r] not in seen:
                max_len = max(max_len, (r - l + 1))
                seen.add(s[r])
                r += 1
            else:
                while s[r] in seen and l<=r:
                    seen.remove(s[l])
                    l+=1
        
        return max_len