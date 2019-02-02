/*Inverteded Binary Tree*/
#include <iostream>
#include <algorithm>


using namespace std; 


struct TreeNode {
    int val; 
    TreeNode *left;
    TreeNode  *right;
    TreeNode(int x): val(x), left(NULL), right(NULL){ }
};

// obv want to swap left and right nodes as we traverse left
// or rigth 
// if there exists a root -> do swaps
// if there doesnt return null since the root does not exist 
// since passing pointers do not have to return values to 
// keep track of order 
TreeNode* invertedBinaryTree(TreeNode* root) {
    if (root) {
            invertedBinaryTree(root->left);
            invertedBinaryTree(root->right);
            swap(root->left, root->right);    
    }
    return root;

}


