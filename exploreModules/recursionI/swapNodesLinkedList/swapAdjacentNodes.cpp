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


ListNode* swapPairs(ListNode* head) {
        if(head == NULL) return NULL;
        if(head->next == NULL) return head;
        // set up a pointer to return
        ListNode* next = head->next;
        head->next = swapPairs(next->next);
        next->next = head;
        return next;
    }

int main() {
    return 0; 
}
