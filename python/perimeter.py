class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
      # if the graph contains a neighbor then there will exist no edge
      perimeter = 0
      visited = [[False for _ in range(len(grid[0]))] for i in range(
          len(grid))]  # 2d matrix of false value
      for r in range(len(grid)):
        for c in range(len(grid[r])):
          if grid[r][c] == 1:
            perimeter += self.dfs(r, c, grid, visited, perimeter)
      return perimeter

    # e
    def dfs(self, row, col, grid, visited, perimeter):
      # make sure the positions we go to are valid and
      if visited[row][col] == True or grid[row][col] == 0:
        return 0
      visited[row][col] = True
      if row - 1 >= 0:
        perimeter += self.getPerimeter([row-1, col], grid, perimeter)
        self.dfs(row-1, col, grid, visited, perimeter)
      if col - 1 >= 0:
        perimeter += self.getPerimeter([row, col-1], grid, perimeter)
        self.dfs(row, col-1, grid, visited, perimeter)

      if row + 1 < len(grid):
        perimeter += self.getPerimeter([row+1, col], grid, perimeter)
        self.dfs(row+1, col, grid, visited, perimeter)

      if col + 1 <= len(grid[row]):
        perimeter += self.getPerimeter([row, col+1], grid, perimeter)
        self.dfs(row, col+1, grid, visited, perimeter)

      return perimeter

    # getPerimeter - get the perimeter at each cell by finding the number of valid neighbors the cell has

    def getPerimeter(self, coord, grid, perimeter):
      # get the directional vectors of every coordinate that is valid
      x = [0, 0, -1, 1]
      y = [1, -1, 0, 0]
      directional = []
      for i in range(4):
        x1, y1 = coord
        x2, y2 = x[i], y[i]
        directional.append([x1+x2, y2+y1])
      # want to check how many valid neighbors
      validNeighbors = 0
      for coord in directional:
        x, y = coord
        if y >= 0 and x >= 0 and x < len(grid) and y < len(grid[x]) and grid[x][y] == 1:
            validNeighbors += 1
      # equivalently these are the number of edges around the current node being visited
      perimeter += abs(4 - validNeighbors)
      return perimeter

# more accurate solution 
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for row in range(len(grid)):
          for col in range(len(grid[row])):
            if grid[row][col]:
              perimeter += 4
              if row and grid[row-1][col]:
                perimeter -= 2
              if col and grid[row][col-1]:
                perimeter -= 2
        return perimeter
