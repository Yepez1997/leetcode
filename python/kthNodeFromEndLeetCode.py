# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
      dummy = ListNode(0)
      dummy.next = head
      first = dummy
      second = dummy
      for i in range(n+1):
        second = second.next
      while second is not None:
        first = first.next
        second = second.next
      first.next = first.next.next
      return dummy.next

