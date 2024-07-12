'''
This solution works but it could be refactored to use a single function instead of defining a secondary dfs function
inside of this function.  The way you could indicate that this type of refactor is possible is by noticing that the dfs
function that you have defined takes the same inputs as the original function.  There are no secondary parameters
required to determine whether or not the two trees are equal so we may be able to just use the top level function.
'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      is_bal = [True]

      def dfs(p,q):
        if (p is None and q is None) or not is_bal[0]:
          return
        
        if (p is None and q is not None) or (p is not None and q is None) or p.val != q.val:
          is_bal[0] = False
          return
        
        dfs(p.left,q.left)
        dfs(p.right,q.right)
      
      dfs(p,q)
      return is_bal[0]

        