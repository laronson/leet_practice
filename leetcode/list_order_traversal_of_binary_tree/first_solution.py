'''
This solution works but it is not optimized.  One way in which we can optimize is to use pythons deque object (combo of
stack and queue) to hold our nodes during the traversal instead of using a list.  The reason why using a deque is more
optimized is because lists are optimized for fixed length operations and although they have queue like behavior (O(n)
time complexity for pop(0)) queues are better because they can pop from both the left and right side of the list in O(1)
time.
'''

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      if not root:
        return []
      
      trace_stack,output = [root],[]

      while len(trace_stack) > 0:
        level_list = []
        for i in range(len(trace_stack)):
          node = trace_stack.pop(0)
          if node:
            level_list.append(node.val)
            trace_stack.append(node.left)
            trace_stack.append(node.right)
        if len(level_list) > 0:
          output.append(level_list)
      
      return output