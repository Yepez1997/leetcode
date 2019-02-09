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
ListNode* swapPairs(ListNode* head) {
        if(head == NULL) return NULL;
        if(head->next == NULL) return head;
        // set up a pointer to return
        ListNode* next = head->next;
        // reverse the process & advance head pointer 
        head->next = swapPairs(next->next);
        // point the next next pointer back to the front 
        next->next = head;
        return next;
    }

    // iteratively with two pointers

int main() {
    return 0; 
}
