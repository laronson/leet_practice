"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

'''
1 <-> 2 <-> 3 <-> 4
        <-> 4
[[2],[1,3,4],[2, 4], [2,3]]

1. How are we going to traverse the original list?
  - BFS search
  - Keep track of visited nodes in a set
2. How are we going to create a copy of each node in our new list?
  - Use a dictionary to keep track of nodes we have already created to use in future neighbor lists

1. check if input node is None -> return None
2. init deque for BFS search and init dummy node to hold reference to front of copied graph
3. Push first node onto deque and add first node to visited list
4. iterate while deque has values:
  - pop top node off of deque
  - if we have already visited popped node -> continue
  - if we have created node already in our node dictionary, get that node, otherwise create a new node
  - create or get neighbor nodes from the node we are observing and push onto neighbors list of new node and onto deque
  - add node we have just added to the graph onto the visited set
5. return dummynode.neighbors[0]

1 <-> 2 <-> 3 <-> 4
        <-> 4
dummyNode = Node(None, [Node(node.val)])
currNode= dummyNode.neighbors[0]
'''
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
      if not node:
        return
      
      q = deque([node])
      visited = set()

      nodeDict = {node:Node(node.val)}

      while q:
        curr = q.popleft()
        if curr.val in visited:
          continue 

        visited.add(curr.val)
        for n in curr.neighbors:
          if n not in nodeDict:
            nodeDict[n] = Node(n.val,[])
          newNeighbor = nodeDict[n]
          nodeDict[curr].neighbors.append(newNeighbor)
          q.append(n)
      
      return nodeDict[node]



        