# ListNode class for Linked List 
class ListNode:
    def __init__(self, val, nextNode=None):
        self.val = val
        self.nextNode = nextNode 


# Reverse a Linked List Iterative 
class ReverseLinkedList:
    def reverseLL(self, head):
        dummy = ListNode(0) 
        curr = head 
        while curr:
            nextNode = curr.next 
            curr.next = dummy 
            dummy =  curr 
            curr = curr.nextNode
        return dummy.next