# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
      # do a inorder traversal
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

      # add sum if range is satisfied
      rangeSum = 0
      for num in inOrder:
        if num >= L and num <= R:
          rangeSum += num

      return rangeSum

