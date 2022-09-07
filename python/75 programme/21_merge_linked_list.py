class node: 
    def __init__(self, data = None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node() 
    
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    
    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        print(elems)
    
    def join_node(self, n = node): #this connects the head node to a new node given
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = n

        
item1 = linked_list()
item1.append(2)
item1.append(2)
item1.append(8)
item1.display()

item2 = linked_list()
item2.append(1)
item2.append(3)
item2.append(4)
item2.display()
   
class Solution:
    count = 0

    def mergeTwoLists(self, a: node , b : node): #this code only works if both linked lists are already in ascending order.
        cur = None
        self.count +=1
        print('Method call' , self.count)
        if a == None: #in case node is not given, return the only available node b (no need to sort)
            return b
        if b == None: 
            return a
        
        if a.data < b.data: #find the smallest node among the two, and reset the node.next to the next smallest node (throuhg recursive function)
            cur = a
            print('item1', a.data,' < item2', b.data)
            print('node' , a, '\n')
            cur.next = self.mergeTwoLists(a.next, b) #this recursive function runs deeper and deeper, at the end, the a/b.next returned to the method is None, hence b/a is returned as the last node.
        else:
            cur = b
            print('item1', a.data,' > item2', b.data)
            print('node' , b, '\n')
            cur.next = self.mergeTwoLists(a, b.next)
        return cur #this returns the starting node
    

  
test = Solution()
new_list = linked_list()
new_list.join_node(test.mergeTwoLists(item1.head.next, item2.head.next))
new_list.display()

item1.display() #note that the original item1 no longer exists since we have relinked the list, they are now part of new_list
item2.display() #note that the original item 2 also no longer exists since we have relinked the list, they are now part of new_list

#test2 = Solution()
#reversed_list = linked_list()
#reversed_list.join_node(test2.reverse_list(new_list.head.next))