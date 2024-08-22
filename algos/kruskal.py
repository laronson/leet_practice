'''
This problem presents us with a node count, n, and a list of edges in a graph, edges, that together represent a 
undirected graph with weighted edges.  The problem asks us to find a minimum spanning tree within the graph whose edges, 
together, total the cheapest combination of edges in an MST possible.  An MST is a minimum spanning tree which 
represents an undirected connected graph that does not have any cycles (Think binary tree).

To do this we could use Prims Algorithm but instead, we have decided to use Kruskals algorithm.  This Algorithm utilizes 
the union-find algorithm combined with a minHeap to find an MST.  The algorithm uses the feature of union-find that is 
able to easily spot if an edge we are going to add will cause a cycle in our graph to ensure we do not add a cycle to 
our MST.  To find the MST, we put all of our edges into a minHeap and then iterate edge by edge to check, in order of 
lowest cost, if edges can be used to make our MST.  If we try to add an edge that will create a cycle, union find will 
tell us and we will skip over that edge.  Like the other graph algos, if we do not hit all edges because the graph is 
not connected, we will not hit them in our algorithm so we will need to check against that if it is a requirement of the 
problem. 
'''

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
      minHeap = [(w,u,v) for u,v,w in edges]
      heapq.heapify(minHeap)
      mst = []

      uf = UnionFind(n)

      while minHeap and len(mst)<(n-1):
        w,u,v = heapq.heappop(minHeap)
        if not uf.union(u,v):
          continue
        mst.append(w)
      
      return sum(mst) if len(mst)==(n-1) else -1

class UnionFind():
  def __init__(self, n):
    self.parents = {node:node for node in range(n)}
    self.rank = {node:0 for node in range(n)}

  def find(self,node):
    p = self.parents[node]
    while p != self.parents[p]:
      self.parents[p] = self.parents[self.parents[p]]
      p = self.parents[p]
    return p
  
  def union(self,n1,n2):
    p1,p2 = self.find(n1), self.find(n2)

    if p1==p2:
      return False

    if self.rank[p1]>self.rank[p2]:
      self.parents[p2]=p1
    elif self.rank[p2]>self.rank[p1]:
      self.parents[p1]=p2
    else:
      self.parents[p2]=p1
      self.rank[p1]+=1
    
    return True

