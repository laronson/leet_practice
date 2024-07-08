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

        bfs_stack = [(root,1)]
        max_depth = 0
        while len(bfs_stack) > 0:
            for i in range(len(bfs_stack)):
                node,depth = bfs_stack.pop()
                if node:
                    max_depth = max(max_depth,depth)
                    bfs_stack.append((node.left, depth+1))
                    bfs_stack.append((node.right, depth+1))
        
        return max_depth


        