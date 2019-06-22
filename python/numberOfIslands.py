class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0
        for row in range(len(grid)):
          for col in range(len(grid[row])):
            if grid[row][col] == '1':
              islands += 1
              self.dfs(grid, row, col)

        return islands

    def dfs(self, grid, row, col):
      if row < 0 or col < 0 or row + 1 > len(grid) or col >= len(grid[0]) or grid[row][col] != '1':
        return False
      grid[row][col] = '0'
      self.dfs(grid, row+1, col)
      self.dfs(grid, row-1, col)
      self.dfs(grid, row, col+1)
      self.dfs(grid, row, col-1)



