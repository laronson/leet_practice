'''
** This solution is not optimal because we do not actually need to do a traversal of all nodes ** 

n:int -> The number of nodes in an undirected graph from 0 - n-1
edges:List[int] -> a list of edges between nodes in the form of [node1,node2] which indicates that there is an edge between node1 and node2
return:int -> the total number of connected components in the graph (aka the number of groupings)

Rules:
  1) undirected graph which means that if there is an edge between a and b, a->b & b->a
  2) Can have groupings of connected nodes that count twards the total 
  3) No duplicate edges in edges list
  4) a standalone node counts as a connected component

  n=4
  edges = [[0 1],[2,3]]
  return 2

  n=4
  edges = [[0 1]]
  return 1

  init adjacency graph
  init visited set
  define our dfs fn o(n)
  for each node in our nodes that we have not yet visited:
      dfs search from that node
      add 1 to connectedComponents
  return connectedComponents
'''

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
      if not edges:
        return n
      
      adjacencyList = self.initAdjacencyList(n,edges)
      visited, connectedComponentsCount = set(),0

      def traverseFromNode(node):
        for n in adjacencyList[node]:
          if n not in visited:
            visited.add(n)
            traverseFromNode(n)
      
      for n in range(n):
        if n not in visited:
          traverseFromNode(n)
          connectedComponentsCount+=1
        
      return connectedComponentsCount
    
    def initAdjacencyList(self, n,edges):
      adjacencyList = {node: [] for node in range(n)}
      for nodeA,nodeB in edges:
        adjacencyList[nodeA].append(nodeB)
        adjacencyList[nodeB].append(nodeA)
      return adjacencyList

        