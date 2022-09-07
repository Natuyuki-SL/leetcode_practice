'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
'''

class Solution:
    def transformString(self, inp): #this method maps unique letters to numbers, everytime they appear for the first time
        index_mapping = {}
        new_string = []
        for (i,n) in enumerate(inp): 
            if n not in index_mapping:
                index_mapping.update({n:i})
            new_string.append(index_mapping.get(n))
        print(new_string)
        return new_string
        
                    
    def isIsomorphic(self, s: str, t: str) -> bool:
        if self.transformString(s) != self.transformString(t):
            return False
        else:
            return True

test1 = Solution()
print(test1.isIsomorphic('paper', 'title'))