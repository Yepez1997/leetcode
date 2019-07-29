"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""

# approach
  # traverse inorder and at each step keep track of elements last
  # once popped off convert to linked list

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        # do a dfs inorder traversal of the tree
        def inOrderDFS(node):
          nonlocal first, last
          if node:
            inOrderDFS(node.left)
            if last:
              last.right = node
              node.left = last
            else:
              # keep track of the smallest element we have seen
              first = node
            last = node
            inOrderDFS(node.right)

        if not root:
          return None

        first = None
        last = None
        inOrderDFS(root)
        # point the last to the first, and last to the first
        first.left = last
        last.right = first

        return first
