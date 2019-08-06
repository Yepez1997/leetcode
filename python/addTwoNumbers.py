# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
      dummyHead = ListNode(0)
      p, q, currentHead = l1, l2, dummyHead
      carry = 0
      while (p is not None or q is not None):
        x = self.getNodeValue(p)
        y = self.getNodeValue(q)
        summed =  carry + x + y
        carry = summed // 10
        currentHead.next = ListNode(summed % 10)
        currentHead = currentHead.next
        if p is not None:
          p = p.next
        if q is not None:
          q = q.next

      # check for overflow
      if carry > 0:
        currentHead.next = ListNode(carry)
      return dummyHead.next

    def getNodeValue(self, node):
      if node is not None:
        return node.val
      else:
        return 0

