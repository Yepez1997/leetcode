#include <iostream>


/*  Problem Statemenent: 
 *   Given two binary trees, write a function to 
 *   check if they are the same or not.
 *   Two binary trees are considered the same 
 *   if they are structurally identical 
 *   and the nodes have the same value.
 */

using namespace std; 

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x): val(x), left(NULL), right(NULL) {}
};

// The algorithm halts when left side does not equal the right side 
    // in respect to the value 
    // and the structure 
// algorithm succeeds when both left and right are null in that case 
// return leftTree == rigthTree which translates to NULL == NULL -> True
bool isSameTree(TreeNode* leftTree, TreeNode* rightTree) {
    if (leftTree == NULL || rightTree == NULL) {
        return leftTree == rightTree;
    }
    return (leftTree->val == rightTree->val && isSameTree(leftTree->left,rightTree->left) 
    && isSameTree(leftTree->right, rightTree->right));
    
}




