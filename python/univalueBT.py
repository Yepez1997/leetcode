# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        unival = root.val
        queue = [root]
        while queue:
          node = queue.pop()
          if node.val != unival:
            return False
          if node.left:
            queue.append(node.left)
          if node.right:
            queue.append(node.right)
        return True


