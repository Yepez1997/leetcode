''' check if there is a cycle in the graph ''' 
# can do a topological approach or perhaps keep track of the elements visited in a stack 
def checkCycle(graph):
    seen = set() # or visited 
    # explore the graph 
    for vertex in graph.keys():
        if vertex not in seen:
            if exploreGraph(vertex, seen, graph):
                return True 
    return False

        
''' exploreGraph - simple dfs traversal '''
def exploreGraph(vertex, seen, graph):
    # base case to check if there is a cycle
    # or do the visiting/visited methods  
    if vertex in seen:
        return True 
    # add the value to seen 
    seen.add(vertex)
    # go through all the verticies 
    for v in graph[vertex]:
        if exploreGraph(v, seen, graph):
            return True 
    return False 
        

    






