'''
This solution presents us with a string consisting of only upper-case english characters and an integer k, which
represents the number of characters that we are able to change within the string.  The goal of this problem is to find
the longest substring within s that has only one repeating character after we swap k letters.  For example, if we are
given s="XYYX" and k=2 the longest substring would be 4 after we either change the two Ys to Xs or vise versa to make a
string like "XXXX".  If we were given s="XYWZ" and k=2 then the longest substring would be 3 because we could only
change two of the letters to match one of the others.

To solve this problem we can use a "snaking" window technique to snake through the substrings of s.  We start with a
left and right pointer at the begining of s. For each iteration we move the right pointer one character and check each substring,
to see if the amount of letters we can change (k) is equal to the number of letters we would need to change
(sum(all_letters_in_substring)-max(letter_in_the_substring)).  If the number of letters we would need to change is
greater than k, then we move the left pointer to the right until k <= the number of letters we need to change.  At that
point, we measure the length of that substring and compare it to the max substring we have already seen.

This solution works and has a runtime of O(n*26) and a memory of O(26).  We can refactor to make the performance and
space complexity a bit better.  These refactors are in the second solution.  
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r, max_len = 0,0,1
        letter_counts = [0]*26

        while r<len(s):
            letter_code = ord(s[r])-ord('A')
            letter_counts[letter_code] += 1

            while  k < (sum(letter_counts) - max(letter_counts)) and l<=r:
                letter_code = ord(s[l])-ord('A')
                letter_counts[letter_code] -= 1
                l += 1
            
            max_len = max(max_len, (r-l+1))
            r += 1
        
        return max_len

