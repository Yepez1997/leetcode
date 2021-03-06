/* Programa finds the number of islands in a graph using BFS */
#include <algorithm> 
#include <iostream>
#include <queue>
#include <iterator>
#include <iostream>
#include <vector>
#include <utility>

using namespace std;

// do a type def coordinates 
typedef pair<int, int> coordinates; 

int numIslands(vector<vector<char> > &grid) {
    int nr = grid.size(); 
    if (!nr) return 0; 
        int nc = grid[0].size(); 
        int num_islands = 0;
    for (int r = 0; r < nr; ++r) { 
        for (int c = 0; c < nc; ++c) {
            if (grid[r][c] == '1') {
                ++num_islands; 
                grid[r][c] = '0'; // mark as visited
                // find all neighbors 
                queue<coordinates > neighbors; 
                // change the rest to make pair
                neighbors.push(make_pair(r,c));
                while (!neighbors.empty()) {
                    coordinates rc = neighbors.front(); 
                    neighbors.pop(); 
                    int row = rc.first;
                    int col = rc.second; 
                            
                    if (row - 1 >= 0 && grid[row - 1][col] == '1') {
                        neighbors.push(make_pair(row - 1, col));
                        grid[row - 1][col] = '0'; 
                    }

                    if (row + 1 < nr && grid[row + 1][col] == '1') {
                        neighbors.push(make_pair(row + 1, col));
                        grid[row + 1][col] = '0'; 
                    }

                    if (col - 1 >= 0 && grid[row][col - 1] == '1') {
                        neighbors.push(make_pair(row, col - 1)); 
                        grid[row][col - 1] = '0'; 
                    }

                    if (col + 1 < nc && grid[row][col + 1] == '1') {
                        neighbors.push(make_pair(row, col +  1)); 
                        grid[row][col - 1] = '0'; 
                    }
                }
            }
        }        
    }
}



