'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class IterativeSolution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        ans = []
        cur = root
        while True:
            if cur != None:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                ans.append(cur.val)
                cur = cur.right
            else:
                break
        return ans

class RecursiveSolution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def _inorderTraversal(root):
            if root:
                _inorderTraversal(root.left)
                ans.append(root.val)
                _inorderTraversal(root.right)
        _inorderTraversal(root)
        return ans
