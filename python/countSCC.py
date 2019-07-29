class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
      # in other words do a standard dfs
      def exploreGraph(graph, visited, vertex):
        if visited[vertex]:
          return
        # visit the vertex
        visited[vertex] = True
        for neighbor in graph[vertex]:
          exploreGraph(graph, visited, neighbor)

      visited = [False for _ in range(n)]
      connectedComponents = 0
      graph = [[] for _ in range(n)]
      # apparently the graph had to be undirected
      for edge in edges:
        fromEdge, toEdge = edge[0], edge[1]
        graph[fromEdge].append(toEdge)
        graph[toEdge].append(fromEdge)

      for i in range(n):
        if not visited[i]:
          connectedComponents += 1
          exploreGraph(graph, visited, i)

      return connectedComponents
