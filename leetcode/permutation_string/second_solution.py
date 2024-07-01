'''
This solution uses a match counter to check if the letters in a substring in s2 are a permutation of s1.  To do this, we
first get a letter count of s1 and a letter count of the first substring of lenth(s1) in s2.  We then use the letter
count of s1 and the letter count of the first permutation of s2 to generate a match count which is an int in range from
0-26.  The number represents the number of letters in a substring of s2 that match the number of letters in s1.  That
way, instead of using a letter_count array to check the letters in s1 vs a substring of s2, we can keep track of our
match count as we look at substrings in s2.  If the match count ever equals 26, then we can say that there is a
substring in s2 that is a permutation of s1. 

One thing of ntoe, when iterating through s2 checking each substring we need to add a clause to our match count
increase/decrease conditionals to make sure we do not increment our match count at the wrong times.  When changing our
letter counts when we increment l or r we need to check to see if that move had flipped the letter count in a way that
changed the match value at that letter. We add a clause to protect us against decrementing the match count if the match 
was set to be wrong during our initial match count (lines 17-19) and our change made by moving the l pointer keeps the 
match count for this letter wrong.  For example, if the s1=abc and s2=bbbca.  The initial match count will have
-1 due to the 3 Bs at the start of s2.  When we first move l to the right and set the b count from 3 to 2,
the letter counts will still be wrong but we do not want to decrement matches because it was already wrong.
Because we are only ever increasing or decreasing s2_counts by 1, checking to see if the s2_count is one
off from the count in s1 ensure that we only decrease or increase matches when the change we make by moving
the l and r pointers affects the match
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 

        s1_count= [0]*26
        s2_count = [0]*26
        matches = 0

        #This loop is dual purposed.  We use it to get the letter count of s1 and to check the first substring of
        #length len(s1) in s2.  That way, once we start to slide our window in s1, we have already checked the first
        #substring that could be a permutation of s1
        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord('a')] += 1
            s2_count[ord(s2[i])-ord('a')] += 1

        for (lc1,lc2) in zip(s1_count,s2_count):
            if lc1 == lc2:
                matches += 1

        l,r=0,len(s1)-1
        while r<len(s2):
            if matches == 26:
                return True
            
            s2_count[ord(s2[l])-ord('a')] -= 1
            if s2_count[ord(s2[l])-ord('a')] == s1_count[ord(s2[l])-ord('a')]:
                matches += 1
            #This clause is here to protect us against decrementing the match count if the match was set to be wrong
            #during our initial match count (lines 17-19) and our change made by moving the l pointer keeps the match
            #count for this letter wrong.  For example, if the s1=abc and s2=bbbca.  The initial match count will have
            #-1 due to the 3 Bs at the start of s2.  When we first move l to the right and set the b count from 3 to 2,
            #the letter counts will still be wrong but we do not want to decrement matches because it was already wrong.
            #Because we are only ever increasing or decreasing s2_counts by 1, checking to see if the s2_count is one
            #off from the count in s1 ensure that we only decrease or increase matches when the change we make by moving
            #the l and r pointers affects the match
            elif s2_count[ord(s2[l])-ord('a')] == s1_count[ord(s2[l])-ord('a')] - 1:
                matches -=1
            
            l+=1
            r+=1

            if r < len(s2):
                print(s2[r])
                s2_count[ord(s2[r])-ord('a')] += 1
                if s2_count[ord(s2[r])-ord('a')] == s1_count[ord(s2[r])-ord('a')]:
                    matches += 1
                elif s2_count[ord(s2[r])-ord('a')] == s1_count[ord(s2[r])-ord('a')] + 1:
                    matches -=1
        
        return matches == 26 

