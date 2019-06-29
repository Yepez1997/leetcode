# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        inOrder = []
        stack = []
        while stack or root:
          if root:
            stack.append(root)
            root = root.left
          else:
            node = stack.pop()
            inOrder.append(node.val)
            root = node.right
        return inOrder


