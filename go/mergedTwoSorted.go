func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
    // compare the first list of l1 and te the first list of l2;
    merged := &ListNode{};
    dummyHead := merged 
    for (l1 != nil || l2 != nil) {
        if (l1 == nil) {
            dummyHead.Next = l2
            break
        }
        if (l2 == nil) {
            dummyHead.Next = l1
            break
        }
        if (l1.Val < l2.Val) {
            dummyHead.Next = l1
            l1 = l1.Next
            //merged = merged.Next
        } else {
            dummyHead.Next = l2
            l2 = l2.Next
            //merged = merged.Next
        }
        dummyHead = dummyHead.Next 
    }
    return merged.Next;

}
