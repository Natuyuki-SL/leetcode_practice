# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        cur = head
        memory = []
        while cur.next != None:
            memory.append(cur)
            cur = cur.next
            if cur.next == None:
                return None
            elif cur in memory:
                return cur
            
            