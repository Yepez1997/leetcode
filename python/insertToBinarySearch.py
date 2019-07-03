# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # first must find the location to insert the binary tree
        # handles the case where the tree node is initialy empty
        if root == None:
          return TreeNode(val)
        # insert to the right subtree
        if val > root.val:
          root.right = self.insertIntoBST(root.right, val)
        else:
          # insert to the left subtree
          root.left = self.insertIntoBST(root.left, val)
        return root

