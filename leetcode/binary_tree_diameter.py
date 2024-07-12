'''
This problem presents us with a binary tree and asks us to find the max diameter within the binary tree.  The diameter 
of any two nodes within a binary tree can be calculated as the path (or number of nodes) that we would need to take to 
traverse from one node to the other.  

To solve this problem, we can traverse through the tree and at each node, find the max depth of the left and right 
subtrees of that node, and then add those two values together to get the max diameter at that node.   We can do this 
recursively using a dfs search where we traverse to the bottom of the left and right sub-trees.  Once we hit the bottom, 
we start passing back the number of nodes we see on the traversal up and use that as the number of nodes to add up when 
we hit any higher nodes.  As we traverse up, we keep track of the max sum(right_sub + left_sub) to keep track of the 
largest diameter we see.  We return the max depth of either the left or right subtree of each node as we traverse back 
up the tree so the next highest node in the tree can use the max-depth of either its left or right sub-trees when 
calculating the diameter at that node.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      res = [0]

      def dfs(node):
        if not node:
          return 0
        
        left_depth = dfs(node.left)
        right_depth = dfs(node.right)

        res[0] = max(res[0], (left_depth + right_depth))

        return max(left_depth, right_depth) + 1
      
      dfs(root)
      return res[0]
        