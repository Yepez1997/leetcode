func maxAreaOfIsland(grid [][]int) int {
    maxIslandSize := 0 
    seen := make([][]bool, len(grid))
    for i, _ := range seen {
        seen[i] = make([]bool, len(grid[0]))
    }
    for row := 0; row < len(grid); row++ {
        for col := 0; col < len(grid[row]); col++ {
            if grid[row][col] == 1 {
                // expore
                islandSize := depthFirstSearch(grid, seen, row, col)
                if maxIslandSize < islandSize {
                    maxIslandSize = islandSize
                }
            }
        }
    }
    
    return maxIslandSize
}

func depthFirstSearch(grid [][]int, seen [][]bool, row, col int) int {
    if (col < 0 || row < 0 || row + 1 > len(grid) || col >= len(grid[0]) || grid[row][col] != 1 || seen[row][col]) {
        return 0 
    } 
    seen[row][col] = true 
    return (1 + depthFirstSearch(grid, seen, row-1,col) + depthFirstSearch(grid, seen, row+1, col) + depthFirstSearch(grid, seen, row, col-1) + depthFirstSearch(grid, seen, row, col+1))
}
