'''
This problem presents us with a binary tree and asks us to return a list of node values that are visible only from the 
right side of the tree.  In other words, return a list of node values that are the right most node on each level.

To do this, we can use a post-order breadth first search to traverse through the array.  This will make sure that as we 
scan through the nodes of each level of the tree, the first non-None node that we encounter will be the rightmost node.  
As we perform the traversal, when we see the rightmost node of each level, add that node’s value to the output array.
'''

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
      right_view = []
      q = deque([root])

      while len(q) > 0:
        first_seen=False

        for i in range(len(q)):
          node = q.popleft()
          if node:
            if not first_seen:
              right_view.append(node.val)
              first_seen=True
            q.append(node.right)
            q.append(node.left)
        
      return right_view
