# general topological sort ? - my work
# courze prequisites in leetcode

class TopologicalSort:

    # verticies is the number of verticies that exist in the graph
    # prereq - list of edges going into a node
    def topoSort(self, verticies, prereq):

        graph = [[] for _ in verticies]
        # keep track of which verticies are visitedi
        visited = [0 for _ in verticies]

        # in other words build the graph
        for pre in prereq:
            x, y = pre
            graph[x].append(y)


        for v in range(verticies):
            if not self.depthFirstSeach(v, visited, graph):
                return False
        return True

    def depthFirstSeach(self, at, visited, graph):
        # check for a cycle
        if visited[at] == -1:
            return False

        if visited[at] == 1:
            return True

        # visit the node
        visited[at] = -1

        for n in graph[at]:
            if not self.depthFirstSeach(n, visited, graph):
                return True
        # once done with the dfs add the last node back or mark it - in this case
        visited[at] = 1
        return True

