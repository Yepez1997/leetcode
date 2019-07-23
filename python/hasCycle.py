# deteramine if a single linked list has a cyle
def hasCycle(head):
    slow = head 
    fast = head 
    while slow != fast:
        if slow is None or fast is None:
            return False 
        slow =  slow.next
        fast = fast.next.next 
    return True 