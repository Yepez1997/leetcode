from Queue import PriorityQueue
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class mergeKLists(object):
    def mergeKLists(self, lists):
        head = point = ListNode(0)
        pq = PriorityQueue()
        # insert the first n then pop off the next n
        for l in lists:
            if l:
                pq.put((l.val, l))

        while not pq.empty():
          val, node = pq.get()
          point.next = ListNode(val)
          point = point.next
          node = node.next
          if node:
            pq.put((node.val, node))
        return head.next


