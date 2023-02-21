'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        if strs[0] == 0:
            return ""
        strs = sorted(strs, key=len)
        ans = strs[0]
        for word in range(1,len(strs)):
            n = 0
            while n < min(len(ans), len(strs[word])):
                if strs[word][n] == ans[n]:
                    n +=1
                else:
                    ans = ans[:n]
                    break
        return ans

class RecursiveSolution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if (strs == None ) or ( len(strs) <= 1):
            return strs[0]

        def com(word, n):
            if word =="":
                return word
            while n < len(strs):
                if word == strs[n]:
                    return com(word, n+1)
                else:
                    new_word = ""
                    i = 0
                    print('Comparing', word, "with", strs[n])
                    for letter in word:
                        if (i< len(strs[n])) and (letter == strs[n][i]):
                            new_word = new_word + letter
                            i +=1
                        else:
                            print(new_word)
                            return com(new_word, n+1)
                    n +=1
            try: return new_word
            except: return word

        return com(strs[0], 1)


