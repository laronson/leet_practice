class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_char = {}
        for c in t:
            t_char[c] = t_char.get(c,0) + 1
        
        s_char = {}
        l = r  = 0
        match_count = 0
        min_string = None
        while r<len(s):
            c = s[r]

            if c in t_char:
                s_char[c] = s_char.get(c,0) + 1
                match_count += 1
                
                while match_count == len(t):
                    if s_char == t_char:
                        min_string = s[l:r+1] if not min_string or len(min_string) > r-l+1 else min_string
                    if s[l] in s_char:
                        s_char[s[l]] -= 1
                        match_count -= 1
                    l += 1
            r+=1
        
        return min_string or ''