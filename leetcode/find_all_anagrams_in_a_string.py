"""
This problem presents us with string s and p and asks us to find all instances of anagrams of p inside of string s and 
return the start indexes of the instances of those anagrams in s.

To do this problem, we must first define what an anagram is.  Two strings are anagrams of one another if both strings 
consist of the same characters and have the same amount of those characters.  Therefore, to find all substrings of s 
that are anagrams of p, we can loop through all substrings in s and find all of the ones that that consist of the same 
characters and character counts as p.  This can be done using a sliding window approach.

To do this efficiently, we can keep track of the character counts in p, the character counts in our substring of s, and 
the number of differences between those two counts.  As we shift our sliding window to the right, we can alter our s 
char counts to reflect the removal of the char to the left of the new substring and the addition of the character at the 
right most position of our new substring.  While we do that, we check to see if that new addition or removal makes it so 
our difference counter, reflecting the differences in our char counts between our current substring of s and p, is 0.  
If the difference count is 0, then we know that our current substring in s is an anagram of p.

To keep track of our differences efficiently, we can alter our difference count as we shift through our substrings of s.  
If the addition of our right character makes it so that our sCount and pCount for that character are equal, then we 
subtract one from our difference counter.  However, if it is not the case that those character counts are equal, we do 
not want to always increase our difference counter because we need to account for the case when the addition of a 
character that exists in p to our substring does not make it so the count of that character are the same in s and p 
(eg p=”aa” and substring moves from “bc” to “ca”).  Therefore, we only want to decrease our difference counter if the 
addition of our new character brings us from a state of s and p having the same count for the added character to a state 
where they are no longer equal.  Because, in the case of adding a new char, the character counts can only go up, it 
would only be the case that a new difference can occur when the new count of that character in sCount is one over the 
count of that character in pCount (aka sCount[char] - 1 == pCount[char]).  Similarly, we need to account for this when 
we remove a character from the left of our substring.  If the removal of the character to the left makes it so that 
characters count is one over the count of that character in pCount (aka sCount[char] + 1 == pCount[char]) then we add to 
our difference count.

Tips and Tricks: 
Two counts that can only increase or decrease by 1 are considered equal when one count has the same numerical value as 
the other count. Therefore, if you need to keep track of the differences between counts as they are changing, you need 
to be concerned with those two counts shifting from a state of being different to a state of being the same or vise 
versa.  If one count increases and that count now equals one more than the other count, that means that the counts moved 
from a state of being the same to a state of being different.  Similarly, if one count decreases and the value of that 
count now equals one less than the other count, that also means that the counts moved from a state of being the same to 
a state of being different.
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        res, pCharCount, sCharCount = [], [0]*26, [0]*26

        #initilize pCharCount
        for c in p:
            pCharCount[ord(c)-ord('a')] = pCharCount[ord(c)-ord('a')] + 1
        
        #initilize sliding window in s
        for i in range(len(p)):
            sCharCount[ord(s[i])-ord('a')] = sCharCount[ord(s[i])-ord('a')] + 1
        
        #compare initial window to get difference Count
        differences = 0
        for i in range(26):
            if pCharCount[i] != sCharCount[i]:
                differences += 1

        #add index of initial window if there are no differences
        if differences == 0:
            res.append(0)

        #move sliding window through s
        l,r = 0, len(p)-1
        while r < len(s)-1:
            removingCharVal = ord(s[l]) - ord('a')
            addingCharVal = ord(s[r+1]) - ord('a') 

            #add character at the right of the new sliding window position
            sCharCount[addingCharVal] = sCharCount[addingCharVal] + 1
            if sCharCount[addingCharVal] == pCharCount[addingCharVal]:
                differences -= 1
            #only add to the difference count if we were in a state where the char counts were equal and they are no longer equal from adding the new char
            elif sCharCount[addingCharVal] - 1 == pCharCount[addingCharVal]: 
                differences += 1
            
            #remove the character to the left of the new sliding window
            sCharCount[removingCharVal] = sCharCount[removingCharVal] - 1
            if sCharCount[removingCharVal] == pCharCount[removingCharVal]:
                differences -= 1
            #only increase the count if we were in a state where the char counts were equal and are no longer equal by remove the char to the left of the new sliding window
            elif sCharCount[removingCharVal] + 1 == pCharCount[removingCharVal]:
                differences += 1
            
            if differences == 0:
                res.append(l+1)
            
            l+=1
            r+=1
        
        return res

        