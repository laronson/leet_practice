def isPalindrome(self, s: str) -> bool:
    #Use a generator for loop and a lambda function (that in this case is a class method) to filter out undesired 
    #letters.  To make this work, you must use the .join() function to join the result of the generator to a string 
    #which essentially casts the return value as a string.
    stripped_string = ''.join(c for c in s if self.isAlpha(c)).lower()
    #stripped_string = str(c for c in s if self.isAlpha(c)).lower() <- THIS DOES NOT WORK
    start, end = 0, len(stripped_string)-1

    while start < end:
        if stripped_string[start] != stripped_string[end]:
            return False
        start += 1
        end -= 1

    return True

def isAlpha(self, c: str)->bool:
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))