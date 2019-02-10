/* Program swaps adjacent linked list nodes */
#include <iostream>
#include <algorithm>

using namespace std;

/* Naive Linked List Data Structure*/
struct ListNode {
    int val; 
    ListNode *next; 
    ListNode(int x) : val(x), next(NULL) {}
};

/*Swaps pairs recursively in linked list*/
ListNode* swapPairsRecursively(ListNode* head) {
        if(head == NULL) return NULL;
        if(head->next == NULL) return head;
        // set up a pointer to return
        ListNode* next = head->next;
        // reverse the process & advance head pointer 
        head->next = swapPairsRecursively(next->next);
        // point the next next pointer back to the front 
        next->next = head;
        return next;
    }


ListNode* swapPairsIteratively(ListNode* head) {
    // do a while loop and check for 
    if(!head) return NULL;
    ListNode curr(0);
    ListNode* tail = &curr;
    while (head && head->next && head->next->next) {
        ListNode* first = head->next;
        ListNode* second = head->next->next; 
        tail->next = second;
        tail->next->next = first;
        tail = tail->next->next; // point to our last place 
        head = head->next; // advance our head pointer 
    }
    // return tail-> next because we do not want to include the one 
    return tail->next; 
}

/*
LOOK AT THIS FOR ITERATIVE REFERENCE

ListNode *swapPairs(ListNode *head) {
    ListNode *dummy = new ListNode(0)
    *node = dummy;
    dummy->next = head;
    while (head && head->next) {
        ListNode *nxt = head->next;
        head->next = nxt->next;
        nxt->next = head;
        node->next = nxt;
        node = head;
        head = node->next;
    }
    // since you dont want zero part of the equation 
    return dummy->next;
}

*/


int main() {
    return 0; 
}
