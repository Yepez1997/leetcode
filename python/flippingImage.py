class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        inverted = []
        for row in A:
          inverted.append([ i^1  for i in row[::-1]])
        return inverted

