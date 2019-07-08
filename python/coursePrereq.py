from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses < 2:
          return True 
        
        graph = [[] for _ in xrange(numCourses)]
        visited = [0 for _ in xrange(numCourses)]
        
        # set up a directed graph 
        for course in prerequisites:
          x, y = course 
          graph[x].append(y)
        
        for i in range(numCourses):
          if not self.dfs(i, visited, graph):
            return False 
        return True 
        
        
    
    def dfs(self, at, visited, graph):
      
      # checks if there is a cycle 
      if visited[at] == -1:
        return False 
      
      if visited[at] == 1:
        return True 
      
      # track the node as visiting 
      visited[at] = -1
      
      for j in graph[at]:
        if not self.dfs(j, visited, graph):
          return False 
      visited[at] = 1
      return True 
        
      
      
    
    