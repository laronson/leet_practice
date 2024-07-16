'''
This problem presents us with a binary tree and asks us to determine if the tree is a valid binary search tree where all 
nodes to the left of a any given node have a value that is less than that node and all nodes to the right of any given 
node have a value that is greater than that node.

To do this, we must consider two things:  First, the node to the left of any given node has a value that is directly 
less than the current node and the node to the right of any given node has a value that is directly greater than the 
current node.  Second, we must make sure that if we are checking the a left node, that nodes value must be within the 
bounds of being less than the directly above it AND if the nodes parent has a parent that the current node is right 
child, the left node of the current node must also be less than that node as well.  Therefore, as we perform a DFS 
search of the binary tree, we must keep track of the parent node and the parent nodes parent so we can properly set 
bounds for the node we are observing.
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
      def isValid(left,right,node):
        if not node:
          return True
        if not (left < node.val < right):
          return False
        
        return isValid(left, node.val, node.left) and isValid(node.val, right, node.right)
      
      return isValid(float('-inf'), float('inf'), root)