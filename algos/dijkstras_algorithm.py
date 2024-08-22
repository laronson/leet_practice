'''
This problem presents us with a node count, n, a list of edges in a graph, edges, and a source node, src.  The problem 
asks us to find the minimum cost it takes for us to get from a single node to all other nodes in a directed graph.

To do this efficiently, we can use Dijkstras Algorithm which is a method to get the shortest path from one node to 
another in a directed graph.  This method is very similar to a BFS search of a tree (which is typically used to get the 
shortest path in a unweighted graph), however there are some slight differences.  To use Dijkstra’s Algorithm, we use a 
minHeap instead of a queue to track the graphs “nearest neighbors”.  Further, when we add a new node to the minHeap, we 
also add the weight of the current node PLUS the aggregated weights of nodes from the path taken to get to that node, 
which we use as the key value of the heap.  We can then traverse the graph like we would in a BFS search but the heap 
will make it so the cheapest path to any node always bubbles up to the top of the heap.  It is guaranteed that every 
time we pop a value off of the heap, it will be the closest and cheapest way to get to that node and therefore, it is ok 
to add duplicates to the heap.  HOWEVER, we can further optimize the algorithm if we simply do not add values to the 
heap once they have appeared in our finalCost data structure that stores the cheapest path values.  Further, every time 
we pop a value off the heap, if it is the first time we have seen that value come off the heap, we can write that nodes 
value to our cost data structure.

Once the algorithm has completed, we will have a full list of all nodes that we visited and the smallest cost it took to 
get to that node from the source.  HOWEVER, we must remember that not all nodes in the graph may be connected.  
Therefore, if the return of our algorithm needs to contain all nodes we must fill our result in with nodes we have not 
visited.
'''

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
      adj = {n:[] for n in range(n)}
      for n1,n2,w in edges:
        adj[n1].append((w,n2))

      return self.findShortestPaths(src,adj)
    

    def findShortestPaths(self,src,adj):
      costs = {}
      minHeap = [(0,src)]

      while minHeap:
        cost,n = heapq.heappop(minHeap)
        costs[n]=cost
        
        if len(costs)>=(len(adj)):
          return costs

        for weight,nextNode in adj[n]:
          if nextNode not in costs:
            heapq.heappush(minHeap,(weight+cost,nextNode))
      
      for n in range(len(adj)):
        if n not in costs:
          costs[n]=-1
      return costs
        





      
