'''Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.



Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        cur1, cur2 = root, root
        stack1 = []
        stack2 = []
        while True:
            if cur1 and cur2:
                stack1.append(cur1)
                stack2.append(cur2)
                if cur1.val + cur2.val == k:
                    return True
                else:
                    cur1 = cur1.left
                    cur2 = cur2.right
                while cur2.val > k:
                    if stack2:
                        cur2 = stack2.pop()
                    else:
                        cur2 = cur2.left
                if cur1.val + cur2.val < k:
                    cur1 = cur1.right
                if cur1.val + cur2.val > k:
                    cur1 = cur1.left
            if stack1:
                cur1 = stack1.pop()



