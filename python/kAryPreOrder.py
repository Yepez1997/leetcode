"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
          return []
        stack = [root]
        preOrder = []
        while stack:
          node = stack.pop()
          preOrder.append(node.val)
          for child in node.children[::-1]:
            stack.append(child)
        return preOrder



