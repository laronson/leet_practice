'''
This solution works as a recursive solution with time and memory complexities of O(log(N)) where n is the number of
nodes in the binary search tree.  The speed is O(log(N)) because we are searching in a binary search tree will, because
of the tree's organization, we will be able to skip nodes that we search (similar to why binary search is log(n)).
However, because this solution is recursive, the memory complexity is also log(n).  We an perform this search
iteratively to make our solution run in constant time.
'''
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
      if not root:
        return

      if root.val < p.val and root.val < q.val:
        return self.lowestCommonAncestor(root.right,p,q)
      elif root.val > p.val and root.val > q.val:
        return self.lowestCommonAncestor(root.left,p,q)
      else: 
        return root