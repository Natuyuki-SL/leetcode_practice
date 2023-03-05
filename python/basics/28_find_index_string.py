def strStr(haystack: str, needle: str) -> int:
        left = right = index = 0
        while index < len(haystack):
            #print(f'{haystack[index]}, left={left}, right={right}')
            if haystack[index] == needle[right]:
                right +=1
                if right == len(needle):
                    return left
            else:
                index = left
                left +=1
                right = 0
            index +=1
        return -1

testcases = ["sadbutsad", "leetcode", "a", "abc", "mississippi", "mississippi", "aabaaabaaac"]
testcases2 = ["sad", "leeto", 'a', 'c', "issip", "pi", "aabaaac"]

for haystack, needle in zip(testcases, testcases2):
    print(f'{haystack}, {needle}, {strStr(haystack, needle)}')