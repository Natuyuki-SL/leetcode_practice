'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==1:
            mid = 0
        else:
            right = len(matrix)-1
            left = 0
            while left <= right:
                mid = (right + left)//2
                print(mid)
                if matrix[mid][0] == target:
                    return True
                elif target < matrix[mid][0]:
                    try:
                        if target > matrix[mid-1][0]:
                            mid -=1
                            break
                        else:
                            right = mid -1
                    except:
                        break
                elif target > matrix[mid][0]:
                    try:
                        if target < matrix[mid+1][0]:
                            break
                        else:
                            left = mid + 1
                    except:
                        break
            print(mid)

        line = matrix[mid]
        if len(line)==1:
            if line[0] == target:
                return True
        else:
            right = len(line)-1
            print('length of line', right)
            left = 0
            while left <= right:
                print(left, right)
                mid = (right + left)//2
                if line[mid] == target:
                    return True
                elif line[mid] > target:
                    right = mid - 1
                elif line[mid] < target:
                    left = mid + 1
                print('checked position', mid, ', value', line[mid])
        return False


