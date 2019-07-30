''' Problem Add Two Numbers As A Linked List -> You are given two linked lists representing non negative integers 
the results are stored in reverse order such that each of their nodes contain a single digit '''

''' Definition for Singly Linked List'''
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

# time complexity -> O(max(m,n)) where m is one linkedlist and n is the other 
# space complexity -> O(n)
class Solution:
  def addTwoNumbers(self, l1, l2, c=0):
        curr = ListNode(0)
        p, q, dummyHead = l1, l2, curr
        while p or q:
            l1Sum = None if p is None else p.val
            l2Sum = None if q is None else q.val 
            total = l1Sum + l2Sum + c
            nodeTotal = ListNode(total % 10)
            c = total // 10 
            curr.next = nodeTotal
            curr = curr.next
            if p:
                p = p.next
            if q:
                q = q.next
        return dummyHead.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
resultString = ""
while result:
    resultString += str(result.val)
    result = result.next
print("".join(reversed(list(resultString))) == "807")
