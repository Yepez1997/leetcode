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
	if ll.head == nil {
		ll.head = node
		ll.tail = node
		return
	} 
	ll.insertBefore(ll.head, node)
}

func (ll *DoublyLinkedList) setTail(node *Node) {
	if ll.tail == nil {
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
	nodeToInsert.prev = node.prev
	nodeToInsert.next = node
	if node.prev == nil {
		ll.head = nodeToInsert
	} else {
		node.prev.next = nodeToInsert 
	}
	node.prev = nodeToInsert
}

func (ll *DoublyLinkedList) insertAfter(node, nodeToInsert *Node) {
	if nodeToInsert == ll.tail && nodeToInsert == ll.head {
		return 
	}
	ll.remove(nodeToInsert)
	nodeToInsert.prev = node 
	nodeToInsert.next = node.next 
	if node.next == nil {
		ll.tail = nodeToInsert
	} else {
		node.next.prev = nodeToInsert
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
	for node != nil && currentPosition != position {
		currentPosition += 1
		node = node.next
	}	
	if node == nil {
		ll.setTail(nodeToInsert)
	} else {
		ll.insertBefore(node, nodeToInsert)
	}
}

func (ll *DoublyLinkedList) removeNodesWithValue(value int) {
	node := ll.head 
	for node != nil {
		nodeToRemove := node
		node = node.next 
		if (nodeToRemove.value == value) {
			ll.remove(nodeToRemove)
		} 
	}
}

func (ll *DoublyLinkedList) remove(node *Node) {
	if node == ll.head {
		ll.head = ll.head.next
	}
	if node == ll.tail {
		ll.tail = ll.tail.prev
	}
	ll.removeNodeBindings(node)
}
	
func (ll *DoublyLinkedList) containsNodeWithValue(value int) bool {
	node := ll.head
	for node != nil && node.value != value {
		node = node.next; 
		
	}
	return node != nil 
}

func (ll *DoublyLinkedList) removeNodeBindings(node *Node) {
	if node.prev != nil {
		node.prev.next = node.next
	}
	if node.next != nil {
		node.next.prev = node.prev
	}
	node.prev = nil 
	node.next = nil
}
