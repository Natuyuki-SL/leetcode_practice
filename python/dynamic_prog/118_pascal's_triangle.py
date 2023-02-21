'''Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Input: numRows = 1
Output: [[1]]

Input: numRows = 10
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1],[1,7,21,35,35,21,7,1],[1,8,28,56,70,56,28,8,1],[1,9,36,84,126,126,84,36,9,1]]

'''

def generate(numRows):
    n = 1
    ans = []
    for rows in range(numRows):
        ans.append([1 for ele in range(n)])
        n +=1
    n = 2
    while n < numRows:
        for ele in range(1, n):
            ans[n][ele] = ans[n-1][ele]+ ans[n-1][ele-1]
        n +=1
    return ans

ans = generate(2)
print(ans)

