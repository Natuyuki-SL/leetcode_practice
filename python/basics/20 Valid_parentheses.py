def isValid(s: str) -> bool:
    dic = {'(':')', '[':']', '{':'}'}
    def pcheck(s):
        if s == '':
            return True
        n = 0
        while n < len(s):
            cur = s[n]
            try:
                cur2 = s[n+1]
                if cur2 == dic[cur]:
                    s = s[:n] + s[n+2:]
                    print('Passing', s)
                    return pcheck(s)
            except:
                pass

            n +=1
        return False

    return pcheck(s)
        
print(isValid('{[]}'))
