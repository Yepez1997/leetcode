# removeKthNodeFromTheEnd By advancing the pointer up to k times 
# can come up with the edge case such that we are at the end after k iterations 
def removeKthNodeFromEnd(head, k):
	first = head
	second = head
	counter = 0
	while counter < k:
		second = second.next
		counter += 1
	if second is None:
		head.value = head.next.value
		head.next = head.next.next
		return
	while second.next is not None:
		first = first.next
		second = second.next
	first.next = first.next.next

