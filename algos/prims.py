'''
This problem presents us with a node count, n, and a list of edges in a graph, edges, that together represent a 
undirected graph with weighted edges.  The problem asks us to find a minimum spanning tree within the graph whose edges, 
together, total the cheapest combination of edges in an MST possible.  An MST is a minimum spanning tree which 
represents an undirected connected graph that does not have any cycles (Think binary tree).

To do this, we can use Prims algorithm to find an MST within a graph.  Prims Algorithm, is very similar to Dijkstras 
Algorithm in that it keeps track of the minimum costs we have seen as we traverse a weighted graph using a BFS-like 
search leveraging a minHeap.  In short, using a minHeap to store our traversals nearest neighbors as we traverse our 
tree will ensure that the nodes with the cheapest const to traverse to the next node remain on top.  However, because 
this is an undirected graph we need to make a few changes.  First, we must keep track of the nodes we have visited 
because the adjacency list we use to represent our graph will contain connections from both nodes in an edge.  Further, 
when we push edges onto our minHeap, we must keep track of where we came from and where we are going if we want to keep 
track of our traversal in some way.  The visited set may help us though in that we can use the length of the visited set 
to determine if we have visited all nodes in the graph and break early if needed.  Like Dijkstras we must remember that 
if the graph is not fully connected, our algorithm will not visit ever node in the graph so we must account for that 
when we are finished traversing if it is a requirement that we visit every node in the graph.
'''

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
      adj = {n:[] for n in range(n)}
      for n1,n2,w in edges:
        adj[n1].append((w,n2))
        adj[n2].append((w,n1))

      return self.findMST(0,adj)
    

    def findMST(self,src,adj):
      mst = []
      visited=set()
      minHeap = [(0,None,src)]
      heapq.heapify(minHeap)

      while minHeap:
        w,src,dest = heapq.heappop(minHeap)
        if dest in visited:
          continue
        
        print(visited)
        mst.append(w)
        visited.add(dest)
        
        if len(visited)==(len(adj)):
          return sum(mst)

        for weight,nextNode in adj[dest]:
          if nextNode not in visited:
            heapq.heappush(minHeap,(weight,dest,nextNode))
      
      return sum(mst) if len(mst)==len(adj) else -1
        
