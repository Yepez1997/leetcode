#include <iostream>

using namespace std; 

// find the number of unique paths from origin the bottom left
class Solution {
public:
    int uniquePaths(int m, int n) {
        // init rows and cols 
        // this is how to init a dp array the easy way 
        int path[m + 1][n+1];
        // init all colums and rows of the zero index to 1 
        for (int i = 0; i < m; i++) {
            path[i][0] = 1;
        } 
        
        for (int j = 0; j < n; j++) {
            path[0][j] = 1;
        }
        
        for (int i = 1; i < m; i++)
            for (int j = 1; j < n; j++)
                path[i][j] = path[i - 1][j] + path[i][j - 1];
        return path[m - 1][n - 1];
    }
};



