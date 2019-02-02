/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

#ifndef NULL
#ifdef __cplusplus
#define NULL    0
#else
#define NULL    ((void *)0)
#endif
#endif

/*Tree Node definition*/
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
    };

/* Least Common Ancestor Problem */
class LCA {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(!root){
            return NULL;
        }
        // check if the current value is larger than both nodes , go left
        if(p->val < root->val && q->val < root->val){
            lowestCommonAncestor(root->left , p , q);
         // go right
        }
        if(p->val > root->val && q->val > root->val){
            lowestCommonAncestor(root->right , p , q);
        }// my LCA 
        
        return root;
        
    }  
};

// for more info on the problem - > https://en.wikipedia.org/wiki/Lowest_common_ancestor
//

