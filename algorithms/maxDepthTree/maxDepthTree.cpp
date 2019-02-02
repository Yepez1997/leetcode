#include <iostream>
#include <algorithm>

/* Problem Statement
 * Given a Binary Tree 
 * Find the maximum depth of the tree 
 */

 using namespace std; 

/* Tree Structure */ 
struct TreeNode {
    int val; 
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// recursively take the max of both the left and right side of the tree 
int maxDepth(TreeNode* root) {
    if(root == NULL){
        return 0;
    }
    else{
        return max(maxDepth(root->left) + 1,maxDepth(root->right) + 1);
    }
}
