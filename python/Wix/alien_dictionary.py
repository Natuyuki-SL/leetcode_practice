'''
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.


Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
'''


def isAlienSorted(words, order: str) -> bool:
    htable = {}
    for n,letter in enumerate(order):
        htable[letter] = n
      
    
    def check(words, n):               
        while n < len(words)-1:
            left = words[n]
            right = words[n+1]
            if left == right:
                return check(words, n+1)
            if len(left) > len(right):
                short = right
            else:
                short = left
            i = 0
            while True:
                if i == len(short):
                    if short!= left:
                        return False  
                    else:
                        return check(words, n+1)
                elif htable[left[i]] > htable[right[i]]:
                    return False
                elif htable[left[i]] == htable[right[i]]:
                    i +=1
                elif htable[left[i]] < htable[right[i]]:
                    return check(words, n+1)
        return True
    
    return check(words, 0)

print(isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(isAlienSorted(["word","world","row"],"worldabcefghijkmnpqstuvxyz"))
print(isAlienSorted(["apple","app"],"abcdefghijklmnopqrstuvwxyz"))