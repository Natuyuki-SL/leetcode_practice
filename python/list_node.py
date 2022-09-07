#This file is tracked by git

class node: #this class itself is never called, it is the basis of each node, each node contains a data and a variable- next that tell us which is the next node object to go to
    def __init__(self, data = None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node() #this is the head node, it will not be indexable or contain any data, used as an object to point towards the first node
    
    def append(self, data):
        new_node = node(data) #creates a node class object containing the data as new_node
        print('New node @', new_node , 'contains data', new_node.data)
        cur = self.head #this is a cursor to help us navigate the nodes, it is now set to the address of the head node
        while cur.next !=None: #the last node (before adding the new one)'s 'next' attribute is always None, so this infinite loop allows us to move until the last node using the cursor
            cur = cur.next #this sets the cur to the address of the next node's address, then the while loop checks the new cursor's next is it is None
            print('iterate', cur)
        cur.next = new_node #when the next attribute is None, that means its the last node before the new node, hence we assign the new node's address to last node's 'next', effectively linking the last node to the new node.
    
    def length(self):
        cur = self.head
        count = 0
        while cur.next !=None:
            cur = cur.next
            count +=1
        return count
    
    def display(self):
        elems = []
        cur = self.head
        while cur.next !=None:
            cur = cur.next
            elems.append(cur.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("Index out of range")
            return None
        else:
            cur = self.head
            cur_idx = 0
            #these few lines needs an extra count to avoid skipping index[0]
            #cur = cur.next     this is the extra move to ensure 0 is at the first node containing data
            #while cur_idx != index:
            #    cur = cur.next
            #    cur_idx += 1
            while True:
                cur = cur.next
                if cur_idx == index: return cur.data
                cur_idx +=1
            # this is better since it does the extra move inside also

    def erase(self, index):
        if index >= self.length():
            print("Index out of range")
            return None
        else:
            cur = self.head
            cur_idx = 0
            while True:
                last_node = cur #here the last_node is used to keep the address before moving onto the next node
                cur = cur.next
                if cur_idx == index:
                    last_node.next = cur.next #once at the index we want, we will change the last_node's 'next' address to the current 'next' address, effectively skipping the current node. The node still exists but now it is no longer linked.
                    return
                cur_idx +=1

test = linked_list()
test.append('haha')
test.append('alamak')
test.append('anyhow')
print('Length of linked list is', test.length())
test.display()
print('Index at 2 is %s' %test.get(2))
test.erase(1)
test.display()

