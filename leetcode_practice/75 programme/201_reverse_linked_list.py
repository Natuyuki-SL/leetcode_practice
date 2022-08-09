class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

    def append(self, data):
        new_node = ListNode(data)
        cur = head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    
    def display(self, node):
        display_list = []
        cur = node
        display_list.append(cur.val)
        while cur.next != None:
            cur = cur.next
            display_list.append(cur.val)
        print(display_list)

head = ListNode(1)
head.append(2)
head.append(3)
head.append(4)
head.append(5)
print('Original linked list')
head.display(head)


class Solution:
    def reverseList(self, head: ListNode):
        if head == None:
            return None

        store = []
        cur = head
        store.append(cur.val)
        length = 1
        while cur.next != None:
            cur = cur.next
            store.append(cur.val)
            length +=1
            
        cur = head
        store.reverse()
        
        for i in range(length):
            cur.val = store[i]
            cur = cur.next
            
        return head

    def reverseList2(self, head: ListNode): #without rewriting data, using 3 pointers (cur, prev, and forward)
            if head == None:
                return None

            cur = head
            prev = None
            while cur.next != None:
                forward = cur.next #forward points to next node
                cur.next = prev #current node .next written as prev node 
                prev = cur #points prev to current node
                cur = forward    #points current node to next node 
            cur.next = prev #needed to change the last node.next to previous node
            return cur

    def reverseList3(self, head: ListNode): #without rewriting data, using 3 pointers (cur, prev, and forward)
            if head == None:
                return None
            
            cur = head
            if head.next: #if there is a next node
                cur = self.reverseList3(head.next)
                head.next.next = head #makes the next node's next the current node
            head.next = None #current node becomes None
            return cur #returns the next node for recursion (goes deeper and deeper, most far node will return itself since the If statement does not run (no next)

test1 = Solution()

print('ReverseList function')
#test1.display(reverseList(head)
new_head = test1.reverseList3(head)
new_head.display(new_head)