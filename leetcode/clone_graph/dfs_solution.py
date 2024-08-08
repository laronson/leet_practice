'''
This problem presents us with a connected undirected graph and asks us to return a deep copy of that graph.  Each graph 
contains a value and a list of the nodes that it is connected to.

To do this, we could either use a BFS or DFS search of the tree.  Both have relatively similar runtimes but DFS seems to 
be a bit faster and easier to implement/understand.  Therefore we will use a recursive DFS search.

In order to solve this problem, we are going to need to traverse through the original graph, create new nodes to 
represent the nodes in the original list, and insert our newly created nodes into each neighbor list of each new node.  
As we create new nodes, we will store them in a dictionary referenced by the original node (e.g. {[node]:newNode}).  

Our recursive function will accept a node as its input.  The function will be responsible for creating a new node to 
reference the original list’s node in our node dictionary.  If the node we are passed already exists within our node 
dictionary, we have already copied that node and we can return.  Otherwise, we create a new node for the node that we 
are observing in the original list and insert it into our node dictionary.  We then iterate through the original nodes 
neighbors and call our recursive function on those nodes.  When we return from the recursive call, the call we just made 
had ensured the the node it was called with now has a reference to a new node in our node dictionary.  We can then push 
the reference to that new node into the neighbors list of the node we are populating.

Once we have completed our DFS traversal of the original graph, it means that all nodes in the original graph have 
references to new nodes populated with new node neighbors in the node dictionary.  We can then return the node in our 
node dictionary referenced by the original graph’s head. 
'''

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
      if not node:
        return

      nodeDict = {}

      def copyGraph(node):
        if node in nodeDict:
          return

        nodeDict[node] = Node(node.val)
        newNode = nodeDict[node]
        for n in node.neighbors:
          copyGraph(n)
          newNode.neighbors.append(nodeDict[n])
      
      copyGraph(node)
      return nodeDict[node]