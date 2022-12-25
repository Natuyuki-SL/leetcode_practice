# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            cur = head
            values = [cur.val]
            while cur.next != None:
                while cur.next.val in values:
                    if cur.next.next:
                        cur.next = cur.next.next
                    else:
                        cur.next = None
                        break
                cur = cur.next
                if cur:
                    values.append(cur.val)
                else:
                    break
        return head
