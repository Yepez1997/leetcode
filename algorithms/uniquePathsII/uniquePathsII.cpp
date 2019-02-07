#include <iostream>
#include <vector>

using namespace std;

class uniquePathsII {
public:
    int uniquePathsWithObstacles(vector<vector<int > >& obstacleGrid) {
        int r = obstacleGrid.size();
        if(r == 0) return 0;
        int c = obstacleGrid[0].size();
        if(c == 0) return 0;
        if(obstacleGrid[0][0]) return 0;

        // first cell has 1 path
        obstacleGrid[0][0] = 1;

        // first row all are '1' until obstacle (from left only) iterate all columns 
        for(int i=1; i<c; i++){
            // 0 is false so chose the falsy condition
            obstacleGrid[0][i] = obstacleGrid[0][i] ? 0 : obstacleGrid[0][i-1];
        }

        // iterate all rows at col 0 
        for(int j=1; j<r; j++){
            // first column is like first row (from top only)
            obstacleGrid[j][0] = obstacleGrid[j][0] ? 0 : obstacleGrid[j-1][0];

            // others are up+left
            for(int i=1; i<c; i++){
                obstacleGrid[j][i] = obstacleGrid[j][i] ? 0 : (obstacleGrid[j-1][i] + obstacleGrid[j][i-1]);
            }
        }
        return obstacleGrid[r-1][c-1];
    }
};



