'''
This problem presents us with a binary tree and asks us to determine whether or not the tree is balanced.  A balenced 
tree is defined as a tree where every node has a left and right subtree who’s depths only differ by 1 or less.

To solve this problem, we can perform a dfs search of the tree, keeping track of the depth of the tree as we traverse 
down.  Once we hit the base case of node is None, we return a list containing the depth of the node that led to the base 
case and True to represent that a node that is None is a balanced tree.  At every node as we traverse up the tree and, 
using the depths of the left and right subtrees, we can determine if the tree at that node is balanced using 
abs(left_depth - right_depth)≤1.  However, because a higher node can be balanced while a lower node can be unbalanced, 
we need to check if the current node is balanced AND if any of the nodes in that nodes subtree is balanced.  Those three 
values together will determine if the current node is balanced.  We return that boolean value as well as the max depth 
of the node so we can use that value at the next node we visit on our traversal up the tree. 
'''

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:       
      def dfs(node,depth):
        if not node:
          return [True,depth-1]
        
        is_left_bal, left_depth = dfs(node.left, depth+1)
        is_right_bal, right_depth = dfs(node.right, depth+1)
        
        return [(is_left_bal and is_right_bal and abs(left_depth - right_depth) <= 1), max(left_depth,right_depth)]

      return dfs(root,1)[0]