'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

class Solution:
    def append(self, head, data):
        new_node = ListNode()
        cur = head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
        cur = new_node
        cur.val = data
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ''
        n2 = ''
        print(l1)
        cur = l1
        n1 = n1 + str(cur.val)
        while cur.next != None:
            cur = cur.next
            n1 = n1 + str(cur.val)
        
        cur = l2
        n2 = n2 + str(cur.val)
        while cur.next != None:
            cur = cur.next
            n2 = n2 + str(cur.val)
        
        print(n1)
        reverse_n1 = n1[::-1]
        print(n2)
        reverse_n2 = n2[::-1]
        
        ans = int(reverse_n1) + int(reverse_n2)
        ans = str(ans)
        ans = ans[::-1]
        print(ans)
        
        start_node = ListNode(ans[0])
        
        for i in range(1,len(ans)):
            self.append(start_node, ans[i])
        
        print(start_node)
        return start_node
        
            
                

 