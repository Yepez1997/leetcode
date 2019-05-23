func reverseList(head *ListNode) *ListNode {
    dummyNode := &ListNode{};
    node := head; 
    for node != nil {
        n := &ListNode{Val: node.Val}
        n.Next = dummyNode.Next
        dummyNode.Next = n
        node = node.Next
    }
    return dummyNode.Next
}
