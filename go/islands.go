func dfs(grid [][]byte, row int, col int) {
    if (row < 0 || col < 0 || row >= len(grid) || col >= len(grid[0]) || grid[row][col] == '0') {
        return 
    }
    grid[row][col] = '0'
    dfs(grid, row + 1, col)
    dfs(grid, row - 1, col)
    dfs(grid, row, col + 1)
    dfs(grid, row, col - 1)
    
}

func numIslands(grid [][]byte) int {
    numIslands := 0
    for row := 0; row < len(grid); row++ {
        for col := 0; col < len(grid[0]); col++ {
            if grid[row][col] == '1' {
                numIslands++
                dfs(grid, row, col)
            }
        }
    }
    return numIslands 
}
