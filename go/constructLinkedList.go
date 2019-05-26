package program

type Node struct {
	value      int
	prev, next *Node
}

type DoublyLinkedList struct {
	head, tail *Node
}

func NewDoublyLinkedList() *DoublyLinkedList {
	return &DoublyLinkedList{}
}

func (ll *DoublyLinkedList) setHead(node *Node) {
	if (ll.head == nil) {
		ll.head = node
		ll.tail = node
		return
	} 
	ll.insertBefore(ll.head, node)
}

func (ll *DoublyLinkedList) setTail(node *Node) {
	if (ll.tail == nil) {
		ll.setHead(node)
		return 
	}
	ll.insertAfter(ll.tail, node)
}

func (ll *DoublyLinkedList) insertBefore(node, nodeToInsert *Node) {
	if nodeToInsert == ll.head && nodeToInsert == ll.tail {
		return 	
	}
	ll.remove(nodeToInsert)
	nodeToInsert.next = node
	nodeToInsert.prev = node.prev
	if node.prev != nil {
		node.prev.next = nodeToInsert
	} else {
		ll.head = nodeToInsert 
	}
	node.prev = nodeToInsert
}

func (ll *DoublyLinkedList) insertAfter(node, nodeToInsert *Node) {
	if (nodeToInsert == ll.tail && nodeToInsert == ll.head) {
		return 
	}
	ll.remove(nodeToInsert)
	nodeToInsert.prev = node 
	nodeToInsert.next = node.next 
	if (node.next != nil) {
		node.next.prev = nodeToInsert
	} else {
		ll.tail = nodeToInsert
	}
	node.next = nodeToInsert
}

func (ll *DoublyLinkedList) insertAtPosition(position int, nodeToInsert *Node) {
	if position == 1 {
		ll.setHead(nodeToInsert)	
		return 
	}
	node := ll.head
	currentPosition := 1
	// traverse until the position is found 
	for (node != nil && currentPosition != position) {
		currentPosition += 1
		node = node.next
	}	
	if node.next == nil {
		ll.setTail(nodeToInsert)
	} else {
		ll.insertBefore(node, nodeToInsert)
	}
}

func (ll *DoublyLinkedList) removeNodesWithValue(value int) {
	node := ll.head 
	for (node != nil) {
		if (node.value == value) {
			ll.remove(node)
		} 
		node = node.next 
	}
}

func (ll *DoublyLinkedList) remove(node *Node) {
	if (node == ll.head) {
		ll.head.next = nil	
		return
	}
	if (node == ll.tail) {
		ll.tail.prev = nil
		return
	}
	ll.removeNodeBindings(node)
}
	
func (ll *DoublyLinkedList) containsNodeWithValue(value int) bool {
	node := ll.head
	for (node != nil) {
		if (node.value == value) {
			return true	
		}
		node = node.next; 
	}
	return false 
}

func (ll *DoublyLinkedList) removeNodeBindings(node *Node) {
	if (node.prev != nil) {
		node.prev.next = node.next
	}
	if (node.next != nil) {
		node.next.prev = node.prev
	}
	node.next = nil 
	node.prev = nil
}
