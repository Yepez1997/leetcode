class Solution(object):
    def inRange(self, grid, r, c):
        numRow, numCol = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= numRow or c >= numCol:
            return False
        return True

    def numIslands(self, grid):
        count = 0 
        row, col = len(grid), len(grid[0])
        for r in range(row):
            for c in range(col):
                tile = grid[r][c]
                if tile == 1: 
                    count += 1   
                    self.dfs(grid, r, c)
                # tile is the actual number 
        return count

    def dfs(self, grid, row, col):
        # check out of bound conditions 
        if not self.inRange(grid, row, col) or grid[row][col] != 1:
            return 
        # visit by placing a zeor 
        grid[row][col] = 0
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)
        
grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0]]

print(Solution().numIslands(grid))
# 3