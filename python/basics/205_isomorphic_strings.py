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
    import itertools
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_t ={}
        map_t_s ={}
        for (a, b) in zip(s, t): #this iterates both lists s and t at the same time
            if a not in map_s_t.keys():
                map_s_t.update({a:b}) #this maps the letter in s to the letter in t
                print("appended", a, b)
            elif a in map_s_t.keys() and b != map_s_t.get(a): #since mapping must be unique, the moment there is a new mapping, we know it is False
                print("wrong pattern")
                return False

        for (a, b) in zip(s, t): #this is the reverse mapping to prevent errors
            if b not in map_t_s.keys():
                map_t_s.update({b:a})
                print("appended", b, a)
            elif b in map_t_s.keys() and a != map_t_s.get(b):
                print("wrong pattern")
                return False
        return True

test1 = Solution()
print(test1.isIsomorphic("egg", "add"))

test2 = Solution()
print(test2.isIsomorphic( "baab" ,"abbb"  ))