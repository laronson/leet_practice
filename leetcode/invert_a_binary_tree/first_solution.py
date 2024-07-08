'''
This is a classic binary tree problem in which we are presented with a binary tree and asked to invert the nodes of the
tree.  This means that the nodes that are in the original tree are perfectly flipped from the original representation of
the tree.

To solve this problem, we can use recursion to visit every node, flip the nodes left and right leafs, and then once
the node's leafs have been flipped, we can recursively visit the leafs and flip the leafs sub-leafs.  The base case for
our recursive function will be when we hit the bottom of the tree at any given node which will be when the left and right
leafs of the current node are both None.  After the base case, we will flip the leafs of the current node.  Then we will
call the invert function recursively on the left and right leafs of the current node. This solution will run in O(n)  
time as we need to visit every node.  It will run with O(n) space because we will add a function call to the stack for 
every node we visit.

This solution is correct and will run with proper time and space constraints, however, there is a better way to code
this in python.  This code is in the second solution.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None

        def invert(node:TreeNode):
            if node.left == None and node.right == None:
                return
            
            tmp = node.right
            node.right = node.left
            node.left = tmp

            if node.left:
                invert(node.left)
            if node.right:
                invert(node.right)
        
        invert(root)

        return root

            
        