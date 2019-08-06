# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # if both p and q are empty this means we traverses all the nodes and conditions thus valid
        if not p and not q:
          return True
        # if either p or q is empty
        if not q or not p:
          return False
        # trivial case to make sure that the values of the nodes are the same
        if p.val != q.val:
          return False
        # recuse both the left and right subtree for left and right
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# ignore this -> just did this randomly 
def reverseLinkedList(node):
    prev = None 
    curr = node 
    while curr:
        nextNode = curr.next 
        curr.next = prev 
        prev = curr
        curr = curr.next
    return prev 
