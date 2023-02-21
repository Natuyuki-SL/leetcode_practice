'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Iterative solution
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        output = []
        cur = root
        while True:
            if cur != None:
                output.append(cur.val)
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                cur = cur.right
            else:
                break
        return output

#recursive solution
class Solution2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        ans = []
        def _traverse(node):
            if node:
                ans.append(node.val)
            if node.left:
                _traverse(node.left)
            if node.right:
                _traverse(node.right)

        _traverse(root)
        return ans
