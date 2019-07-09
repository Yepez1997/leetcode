# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# find the diameter of a binary tree 
# a diameter is defined as the largest distance between each node 
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 1
        # compute the depth of the root

        def dfs(root):
          if root is None:
            return 0
          # the diameter of the tree can be <= left + right + 1
          left = dfs(root.left)
          right = dfs(root.right)
          self.ans = max(self.ans, left + right + 1)
          return max(left, right) + 1
        dfs(root)
        return self.ans - 1
