
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None:
          return []

        queue = [root]
        levelAvg = []
        sumNode = 0
        while queue:
          size = len(queue)
          # count = 0
          for _ in range(size):
            node = queue.pop(0)
            sumNode += node.val
            # count += 1
            if node.left:
              queue.append(node.left)
            if node.right:
              queue.append(node.right)
          levelAvg.append(sumNode / (1.0 * size))
          sumNode = 0
        return levelAvg

