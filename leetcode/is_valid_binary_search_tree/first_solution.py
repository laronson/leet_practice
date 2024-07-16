'''
This solution does not work because we only check to see if the node we are currently looking at is less than (if left
note) or greater than (if right node) the current node.  However, this solution does not consider when a second nested
node does not meet the requirements of a BST for all of its parent nodes.  For example:
      2
     /\
    1  3
    \
     100
In this case, although all triplets of nodes meet the criteria of a BST, the root and the leaf that has a value of 100
does not meet the criteria of a BST because all nodes to the left of the root must be less than 2.
'''

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
      if not root:
        return True
      
      if root.left and root.left.val >= root.val:
        return False
      elif root.right and root.right.val <= root.val:
        return False

      return self.isValidBST(root.left) and self.isValidBST(root.right) 