'''
Invert a Binary Tree 
'''
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    def preorder(self):
        print(self.value)
        if self.left: self.left.preorder()
        if self.right: self.right.preorder()

def invert(node):
    # Fill this in.
    if not node:
        return  
    root.left, root.right = root.right, root.left
    invert(root.left)
    invert(root.right)
    return node  

def invertInorder(node):
    queue = []
    queue.append(node)
    while len(queue) > 0:
        curr = queue.pop(0)
        curr.left , curr.right = curr.right, curr.left 
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return node 

root = Node('a') 
root.left = Node('b') 
root.right = Node('c') 
root.left.left = Node('d') 
root.left.right = Node('e') 
root.right.left = Node('f') 

root.preorder()
# a b d e c f 
print("\n")
invert(root)
root.preorder()