'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

import itertools as it


class Solution:
    def romanToInt(self, s: str) -> int:
        ref = {'I': 1, 
               'V': 5, 
               'X': 10, 
               'L': 50, 
               'C': 100, 
               'D': 500, 
               'M': 1000}
        sum = 0
        
        for roman1, roman2 in it.zip_longest(s, s[1:]):
            print(roman1, roman2, 'current sum', sum)
            sum += ref[roman1]
            if roman2 == None:
                break
            elif ref[roman2] > ref[roman1]:
                sum -= (ref[roman1]*2)
        
        return sum
    
    def romanToInt2(self, s: str) -> int:
        roman_dict = {'I':1, 'V': 5, 'X': 10,'L': 50, 'C': 100, 'D':500, 'M': 1000}
        total = 0
        
        s = s.replace('IV','IIII').replace('IX','VIIII')
        s = s.replace('XL','XXXX').replace('XC','LXXXX')
        s = s.replace('CD','CCCC').replace('CM','DCCCC')
        
        for letter in s:
            total+=roman_dict[letter]
            print(total)
        return total

test = Solution()
#print(test.romanToInt('III'))
#print(test.romanToInt('LVIII'))
print(test.romanToInt('MCMXCIV'))
#print(test.romanToInt2('MCMXCIV'))