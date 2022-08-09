class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
    
class binary_tree:
    def __init__(self):
        self.root = None
       
    def append(self, data):
        if self.root == None:
            self.root = node(data)
        else:
            self._append(self.root, data)
    
    def _append(self, cur_node, data):
        if data < cur_node.data:
            if cur_node.left == None:
                cur_node.left = node(data)    
                cur_node.left.parent = cur_node #set parent - for use of deletion function
                return 
            else:
                self._append(cur_node.left, data) 

        elif data > cur_node.data:
            if cur_node.right == None:
                cur_node.right = node(data)
                cur_node.right.parent = cur_node #set parent - for use of deletion function
                return
            else:
                self._append(cur_node.right, data)
        
        else:
            print('Value already in tree')

    def search(self, target):
        if self.root == None:
            return False
        else:
            return self._search(self.root, target)
    
    def _search(self, cur_node , target):  
        if cur_node.data == target:
            return True #can put node here too, but avoid node to prevent accidentaly writing it

        elif target < cur_node.data and cur_node.left != None:
            return self._search(cur_node.left, target)

        elif target > cur_node.data and cur_node.right != None:
            return self._search(cur_node.right, target)
        
        else:
            return False

    def find(self, data): #this is like search, but it returns the node instead of boolean
        if self.root != None:
            return self._find(self.root, data)
        else:
            return None
    
    def _find(self, cur_node, data):
        if cur_node.data == data:
            return cur_node
        elif data < cur_node.data and cur_node.left != None:
            return self._find(cur_node.left, data)
        elif data > cur_node.data and cur_node.right != None:
            return self._find(cur_node.right, data)
        else:
            return False
    
    def delete_value(self, data): #holder to input data to find the node to delete
        if self.find(data):
            self.delete_node(self.find(data))
        else:
            print('Data not in binary search tree')

    def delete_node(self, cur_node): #actual delete node
        
        def min_value(n): #used to find the smallest value of a node children (to the left)
            cur = n
            while cur.left != None:
                cur = cur.left
            return cur

        def num_children(n): #determines how many children there is.
            num = 0
            if n.left != None: num +=1
            if n.right != None: num +=1
            return num

        parent = cur_node.parent
        children = num_children(cur_node)

        if children == 0: #case 1, no children, just reference the parent left/right to the node
            if parent.left == cur_node: parent.left = None
            else: parent.right = None

        elif children == 1: #case 2, 1 children, rereference the parent left/right to the children
            if cur_node.left == None: child = cur_node.right
            else: child = cur_node.left

            if parent.left == cur_node: 
                parent.left = child
            else: 
                parent.right = child
            child.parent = parent #also reference children to new parent

        elif children == 2: #case 3
            min = min_value(cur_node.right) #check picture, take the smallest node's data of the right child to replace the current node.
            cur_node.data = min.data
            self.delete_node(min) #delete the smallest node (recursive), a case 0 scenario

    def display(self):
        if self.root != None:
            self._display(self.root)
    
    def _display(self, cur_node):
        if cur_node != None:
            self._display(cur_node.left)
            print(cur_node.data)
            self._display(cur_node.right)
        
    def fill_tree(self, num = 100, max_int = 500):
        import random
        for i in range(num):
            element = random.randint(0, max_int)
            #print(element)
            self.append(element)
    
    def height(self):
        if self.root != None:
            return self._height(self.root, 1)
        else:
            return 0
    
    def _height(self, cur_node, h):
        if cur_node == None:
            return h
        left_h = self._height(cur_node.left, h+1)
        right_h = self._height(cur_node.right, h+1)
        return max(left_h, right_h)
        


test = binary_tree()
test.append(1)
test.append(3)
test.append(2)
test.append(7)
test.append(4)
test.append(5)
test.append(20)
test.display()

print('\nSearching and deleting value 4')
print(bool(test.find(4)))
test.delete_value(4)
test.display()


'''
test2 = binary_tree()
test2.fill_tree()
print('Done filling tree')
print()
print('Showing sorted tree')
test2.display()

search = test2.search(48)
if search:
    print(search)
else:
    print('Number not in binary search tree')

print('tree height is', test2.height())
'''




