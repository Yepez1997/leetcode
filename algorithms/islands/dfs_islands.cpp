/*islands: given an n by n grid, each grid contains a '1'  
 * or '0' char. '1' represent land, o/w '0' represents ocean.
 * Find the number of islands in the n x n grid
 * */

// input :
/* 1 | 0 | 0 |
 * 0 | 1 | 1 |
 * 1 | 0 | 0 |
 */

// output -> 3 

//  note this approach uses Depth First Search 
//  can be implemented with BFS and Union Find 
class DFS {
private:
    /*runtime is O(m+n)*/
    void dfs(vector<vector<char>>& grid, int r, int c) {
        
        // number rows
        int nr = grid.size();
    
        // number columns 
        int nc = grid[0].size(); 
        
        /*set current grid to 0*/
        grid[r][c] = '0';
        /* check row down*/
        /if (r - 1 >= 0 && grid[r-1][c] == '1') dfs(grid, r - 1, c); 
        /* check row up*/
        if (r + 1 < nr && grid[r+1][c] == '1') dfs(grid, r + 1, c); 
        /* check colum left */
        if (c - 1 >= 0 && grid[r][c-1] == '1') dfs(grid, r, c - 1); 
        /*check column right */
        if (c + 1 < nc && grid[r][c+1] == '1') dfs(grid, r, c + 1);   
    }
    
public:
    /* do depth first search */
    int numIslands(vector<vector<char>>& grid) {
        /* checks for column size */
        int nr = grid.size(); 
        if (!nr) return 0;
        /* checks row size */
        int nc = grid[0].size(); 
        
        /*int number islands*/ 
        int number_islands = 0; 
        
        /* essentially do dfs */
        for (int r = 0; r < nr; r++){
            for (int c = 0; c < nc; c++) {
                if (grid[r][c] == '1'){
                    number_islands++;
                    dfs(grid, r, c);
                }
            }
        }  
        return number_islands;         
    }
}

int main() {
    
    return 0; 
};
