'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        stack = []
        stack2 = []
        if root:
            stack.append(root)
        while True:
            if stack:
                cur = stack.pop()
                stack2.append(cur)
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
            elif stack2:
                cur = stack2.pop()
                output.append(cur.val)
            else:
                break
        return output

class RecursiveSolution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def _post(root):
            if root:
                if root.left:
                    _post(root.left)
                if root.right:
                    _post(root.right)
                output.append(root.val)
        _post(root)
        return output
