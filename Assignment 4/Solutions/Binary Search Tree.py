class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        ptr_x = self.root
        if ptr_x == None:
            self.root = Node(value)
        else:
            while ptr_x != None:
                ptr_y = ptr_x
                if value < ptr_x.value:
                    ptr_x = ptr_x.left
                elif value == ptr_x.value:
                    return
                else:
                    ptr_x = ptr_x.right
            if value < ptr_y.value:
                ptr_y.left = Node(value)
            else:
                ptr_y.right = Node(value)
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end = ' ')
            self.inorder(node.right)
    
    def preorder(self, node):
        if node:
            print(node.value, end = ' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end = ' ')

values = list(map(int, input().split()))
bst = BST()
for value in values:
    bst.insert(value)

bst.inorder(bst.root)
print()
bst.preorder(bst.root)
print()
bst.postorder(bst.root)