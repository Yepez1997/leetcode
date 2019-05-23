/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <iostream>



using namespace std;


/* Node for Linked List */
struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

/* LinkedListCycle: determaine if there exists a cycle in a singlly linked list */
bool LinkedListCycle(ListNode *head)
{
    ListNode *slow;
    ListNode *fast;
    slow = fast = head;

    // if we reach the end of each pointer -> means no cycle !
    while (slow && fast && fast->next)
    {
        // move fast by two positions -> fast.next.next
        fast = fast->next->next;
        // move slow by one position -> slow.next
        slow = slow->next;

        if (slow == fast)
            return true;
    }
    return false;
}
