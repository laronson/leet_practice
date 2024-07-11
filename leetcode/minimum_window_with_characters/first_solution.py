'''
This solution works but it could be slightly optimized.  Currently, this solution runs in O(s + 26) time and has an
O(26) memory complexity.  We can slightly improve the runtime to come down to O(s) instead of O(s+26) by
keeping track of the number of characters in the substring that match the t string and only run our matching checks if
the number or chars in the window that match t equals the length of t.  That will enable us to skip the need for the
isEqual function check
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_char = {}
        for c in t:
            t_char[c] = t_char.get(c,0) + 1
        
        s_char = {}
        l = r  = 0
        min_string = None
        while r<len(s):
            c = s[r]

            if c in t_char:
                s_char[c] = s_char.get(c,0) + 1
                
                while self.areEqual(t_char, s_char) and l<=r:
                    min_string = s[l:r+1] if not min_string or len(min_string) > r-l+1 else min_string
                    if s[l] in s_char:
                        s_char[s[l]] -= 1
                    l += 1
            r+=1
        
        return min_string or ''


    
    def areEqual(self, t_char, s_char):
        for key in t_char.keys():
            if s_char.get(key, 0) < t_char.get(key):
                return False
        return True