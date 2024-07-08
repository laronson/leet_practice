# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        #Use a stack for dfs traversal and store (stack,depth) as a tuple in the stack 
        dfs_stack = [(root,1)]
        depth = 0
        max_depth = 0
        while len(dfs_stack)>0:
            node,depth = dfs_stack.pop()

            if node:
                max_depth = max(max_depth, depth)
                dfs_stack.append((node.right, depth+1))
                dfs_stack.append((node.left, depth+1))
        
        return max_depth
        