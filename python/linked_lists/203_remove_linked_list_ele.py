'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.



Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
'''

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return None
        cur = head

        #reposition head if the head itself is the val
        while cur and cur.val == val:
            cur = cur.next
            head = cur

        #cycle through nodes
        while cur and cur.next != None:
            prev = cur
            cur = cur.next
            if cur.val == val:
                while cur.next and cur.next.val == val:
                    cur = cur.next
                if cur.next:
                    prev.next = cur.next
                else:
                    prev.next = None
        return head
