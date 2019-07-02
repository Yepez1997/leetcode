"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # if the root is None then return 0 - min height
        if root is None:
          return 0
        # on the stack keep track of the current depth and keep track of the node being processed
        stack = [(root, 1)]
        level = 0
        while len(stack) > 0:
          node, currentLevel = stack.pop()
          if node is not None:
            # i.e if it is not a leaf node take the max of the level the tree is at and the level popped by the node
            level = max(level, currentLevel)
            # iterate each child and add to the stack to iterate with a stack
            for child in node.children:
                stack.append((child, currentLevel + 1))
        return level

