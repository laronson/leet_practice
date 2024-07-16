'''
This problem presents us with a binary tree and asks us to return the level order traversal of the tree as a nested list 
where each sublist in the nested list contains the values of all nodes in the ith level from left to right.

To do this, we can use a breadth first search of the binary tree to traverse the tree level by level.  As we search each 
level, we will keep track of the nodes that we see from left to right and append each levels list of node values to a 
output list once we traverse through the nodes of an entire level.  We can do this using Pythons deque data structure 
to keep track of our nodes during the breadth first search and pull from the front of the queue on O(1) time.
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      if not root:
        return []
      
      q,output = deque([root]),[]

      while len(q) > 0:
        level_list = []
        for i in range(len(q)):
          node = q.popleft()
          if node:
            level_list.append(node.val)
            q.append(node.left)
            q.append(node.right)
        if len(level_list) > 0:
          output.append(level_list)
      
      return output