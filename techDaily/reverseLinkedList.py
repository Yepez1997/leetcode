''' Reverse a linked list recursively and iteratively '''


''' 
    Time Complexity - Recursive and Iterative solution takes O(n) time 
    Space Complexity - Recursive O(n) and Iterative O(1)
''' 


''' Definition for Singly Linked List'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    ''' Drint the list ''' 
    def printList(self):
        node = self
        output = '' 
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
            print(output)

    ''' Iterative solution ''' 
    def reverseIteratively(self, head):
        prev = None
        runner = head
        while runner:
            nextNode = runner.next
            runner.next = prev
            prev = runner
            runner = nextNode
        return prev

    ''' Recursive solution ''' 
    def reverseRecursively(self, head):
        # Implement this.
        if head is None or head.next is None:
            return None 
        node = self.reverseRecursively(head.next)
        head.next.next = head 
        head.next = None
        return node

''' init the test list ''' 
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
testHead.reverseIteratively(testHead)
# testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4