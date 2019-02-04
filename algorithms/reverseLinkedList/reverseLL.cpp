#include <iostream>
#include <algorithm>
#include <vector>



using namespace std; 

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x): val(x) , next(NULL) {}
};

ListNode* reverseLinkedList(ListNode *head) {
    ListNode* prev(NULL);
    ListNode* current = head; 
    while (head != NULL) {
        ListNode* next = current->next;
        current->next = prev;
        prev = current;
        current = next; 
    }
    head = prev; 
    return head; 
}


int main() {
    // first problem:
    // input: 1->2->3->4->5->NULL
    // output: 5->4->3->2->1->NULL
    return 0;
}


