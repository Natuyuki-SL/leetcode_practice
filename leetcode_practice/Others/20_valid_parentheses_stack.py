def isValid(s: str) -> bool:

        dic = {')':'(' , ']':'[' , '}':'{'}
        stack = []
        for i in s:
            if i not in dic:
                stack.append(i)
            else:
                if stack and dic[i] == stack[-1]:
                    print('found', i , 'popped', stack[-1])
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False

print(isValid('[](){}'))
print(isValid('['))
print(isValid('}'))
print(isValid('[()[]]'))
print(isValid('{([]})'))