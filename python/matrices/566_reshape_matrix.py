'''
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.



Example 1:


Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
Example 2:


Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
'''

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        temp = []
        ans = []
        for m in mat:
            for n in m:
                temp.append(n)
        #print(temp)
        if len(temp) != r*c:
            return mat
        for down in range(r):
            row = []
            #n=0
            for across in range(c):
                if temp:
                    #n +=1
                    #print(n)
                    row.insert(0, temp.pop())
            ans.insert(0, row)
            #print(ans)
        return ans




