'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
'''

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        cur = head
        while cur.next != None: # find the length of the list
            cur = cur.next
            length +=1
        length -= n #5 - 2 = 3

        counter = 0
        cur = dummy = ListNode(0)
        dummy.next = head
        while counter <= length: # 0.....3
            prev = cur
            cur = cur.next
            counter +=1
        try:
            prev.next = cur.next
        except:
            print('head is none')
        return dummy.next
