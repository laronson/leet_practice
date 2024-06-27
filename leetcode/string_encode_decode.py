'''
Question: Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

LeetLink: https://leetcode.com/problems/encode-and-decode-strings/
NeetLink: https://neetcode.io/problems/string-encode-and-decode


'''


from typing import List


def encode(self, strs: List[str]) -> str:
    """Encodes a list of strings to a single string.
    """
    encodedString = ""
    for s in strs:
        #String addition in python is simple where you can just use the add operand to concat string together
        #Be careful though, if you are tryting to concat an int with a string, you must convert the int to a string
        #before concatenating 
        encodedString += str(len(s)) + "#" + s
    return encodedString
    

def decode(self, s: str) -> List[str]:
    """Decodes a single string to a list of strings.
    """
    #Destructuring for variable instantiation 
    decodedStrings, idx = [], 0

    while idx < len(s):
        wordIdx = idx
        while s[wordIdx] != '#':
            wordIdx += 1
        #Splicing a string can be done using the : operator inside of a string operation
        length=int(s[idx:wordIdx])
        word=s[wordIdx + 1 : wordIdx + 1 + length]
        
        decodedStrings.append(word)
        idx=wordIdx+1+length

    return decodedStrings
