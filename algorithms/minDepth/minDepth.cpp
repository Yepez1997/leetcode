// Use BFS since bfs gives us the shortest path -> min distance 
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int minDepth(TreeNode* root) {
        queue<TreeNode*> q; int level=0;
        if(root) q.push(root);
        while(!q.empty())
        {
            int size = q.size();
            level++;
            for(int i=0; i<size; i++)
            {
                TreeNode* temp = q.front(); 
                q.pop();        
                if(!temp->right && !temp->left) return level;
                if(temp->right) q.push(temp->right);
                if(temp->left) q.push(temp->left);
            }
        }
            return level;   
        }  
};
