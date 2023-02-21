'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ans = []
        def _check(leftside, rightside):
            if leftside and rightside:
                print(f'checking left {leftside.val} right {rightside.val}')
                if leftside.val == rightside.val:
                    if leftside.left or rightside.right:
                        print('left call')
                        _check(leftside.left, rightside.right)
                    if leftside.right or rightside.left:
                        print('right call')
                        _check(leftside.right, rightside.left)
                else:
                    print('Incorrect value')
                    ans.append(False)
            elif not leftside and not rightside:
                pass
            else:
                print('None call')
                ans.append(False)
        if root.left and root.right:
            _check(root.left, root.right)
        elif root.left or root.right:
            return False
        if ans:
            return False
        else:
            return True
