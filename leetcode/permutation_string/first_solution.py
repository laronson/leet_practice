'''
This problem presents two strings s1 and s2 and we are tasked with determining if s2 contains a substring that is a
permutation of s1.  This means we are finding a substring within s2 that has the exact same letter count (order does not
matter) as s1.

To do this, we first create a letter count array for the characters in s1.  We then create l and r pointers to snake
through s2 and keep track of the letter count for the letters we have seen in s2 at point r.  At each iteration, we
check the count arrays to see if the s2 count is equal to the s1 count.  If it is, we return true. If we hit a character at 
r that makes it so any letter count in the s2 count array is greater than the letter count in s1 for that letter, we 
iterate the l pointer to the right until the letter count at r is back to an equal count OR the l pointer has met up
with r.  If we iterate through s2 and do not ever hit a match, we return false 

This solution actually works and would be accepted.  However, this solution requires us to perform an operation that
checks the letter counts of S1 and S2 every time we iterate making this solution o(n*26)  Although this solution is
still technically O(N) time, the next solution removes the need to perform those O(26) array checking solutions
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
            
        s1_count= [0]*26
        s2_count = [0]*26

        for c in s1:
            s1_count[ord(c)- ord('a')] +=1
        
        l=r=0
        while r<len(s2):
            s2_count[ord(s2[r])-ord('a')] += 1

            if self.count_list_compare(s1_count, s2_count):
                return True
            elif s2_count[ord(s2[r])-ord('a')] > s1_count[ord(s2[r])-ord('a')]:
                while s2_count[ord(s2[r])-ord('a')] > s1_count[ord(s2[r])-ord('a')] and l <= r:
                    s2_count[ord(s2[l])-ord('a')] -= 1
                    l+=1

            r+=1
        
        return False
            


    def count_list_compare(self, l1, l2):
        for i in range(len(l1)-1):
            if l1[i] != l2[i]:
                return False

        return True

