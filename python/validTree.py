class Solution(object):
    def validTree(self, n, edges):
      if len(edges) != n - 1:
          return False
      graph = collections.defaultdict(list)
      for x, y in edges:
          graph[x].append(y)
          graph[y].append(x)
      seen = set()
      # do a dfs once on the root node and if all have beem seem -> valid tree
      def dfs(node):
          seen.add(node)
          for neighbor in graph[node]:
              if neighbor not in seen:
                  dfs(neighbor)
      dfs(0)
      return len(seen) == n
