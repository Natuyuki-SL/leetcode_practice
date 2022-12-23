class Solution:   
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        count = 0
        odd= False
        
        for letter in s:
            if letter not in hashmap:
                hashmap[letter] = 1
            else:
                hashmap[letter] = hashmap.get(letter) +1
        
        print(hashmap)
        for k, v in hashmap.items():
            if v%2 == 0:
                count = count + v   
            if v%2 !=0:
                count = count + (v-1)
                odd = True
        if odd is True:
            return count+1
        else:
            return count

test = Solution()
print(test.longestPalindrome('abccccdd'))
print(test.longestPalindrome('ccc'))
print(test.longestPalindrome('abccqwcasdcdd'))