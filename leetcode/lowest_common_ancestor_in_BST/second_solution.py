'''
This problem presents us with a binary search tree and references to two nodes, p and q, within the binary search tree 
and asks us to find the lowest common ancestor of the two nodes within the BST.  A binary search tree is defined as a 
binary tree where, for each node, any node to the left of that node is less than that nodes value and any node to the 
right of that node is greater than that node value.  The lowest common ancestor of any two nodes within a binary tree is 
defined as the lowest node in the tree that shares the two nodes as decedents.

To solve this problem, we must utilize the organizational structure of the BST to determine how we should traverse the 
tree based off of the values of p and q compared to the current node.  If both p and q have values that are less than 
the current node, then we know that the LCA of the two nodes will be to the left of the current node.   If both p and q 
have values that are greater than the current node, then we know that the LCA of the two nodes will be to the right of 
the current node.  If one of the nodes is greater than or equal to the current node and the other is less than or equal 
to the current node, then we know that we are at the LCA of the two nodes because one of the nodes has to the to the 
left and the other has to be to the right.  

Initially, I solved this problem recursively as I usually do with binary tree problems.  However, with this particular 
problem, it was easy to solve iteratively which decreased the memory complexity of my solution.  The reason why an 
iterative solution makes the most sense here is because the confines of the problem ensure that if we traverse the tree 
correctly, we will hit an answer and we will not need to backtrack through the tree to search previous nodes.  Because 
we do not need to search all of the nodes in the tree (aka use a backtracking solution) we can simply traverse the tree 
iteratively.
'''
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
      curr = root

      while curr:
        if curr.val < p.val and curr.val < q.val:
          return self.lowestCommonAncestor(root.right,p,q)
        elif curr.val > p.val and curr.val > q.val:
          return self.lowestCommonAncestor(root.left,p,q)
        else: 
          return curr