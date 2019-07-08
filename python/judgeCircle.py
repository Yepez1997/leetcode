class Solution:
    def judgeCircle(self, moves: str) -> bool:

        directions = {
            "R": [1, 0],
            "L": [-1, 0],
            "D": [0, -1],
            "U": [0, 1]
        }

        origin = [0, 0]
        start = [0, 0]
        for dir in moves:
          getDir = directions[dir]
          x, y = start
          x1, y1 = getDir
          deltaX, deltaY = x + x1, y + y1
          start = [deltaX, deltaY]
        return True if start == origin else False

