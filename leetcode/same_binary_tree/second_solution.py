'''
The problem presents us with two binary trees and asks us to determine if the binary trees are equal.  Two binary trees 
are equal if they have the same node structure and each node within each tree at the same point have the same value.

To solve this problem, we can perform a dfs search on each tree at the same time (traversing through each tree the same 
way) and check to see if the nodes at each position both exist at the same time (aka the trees have the same structure) 
and if the nodes at that position have the same value.  At first, I did this by declaring a separate dfs function and 
global is_same variable using an array and using the dfs function to iterate through the tress, checking each node for 
node and value equality.  The base case of my function was checking if the nodes passed in were both None and my global 
variable is still True, we return true and continue to iterate through the trees.  If at any point, the nodes are not 
both not None or the value at the nodes are not equal, we set the global is_same variable to false and return.  At that 
point, because our base case inspects the global variable and returns if it is false, traversal will stop and we will 
get a false return value.  Otherwise, if we are able to traverse through the entire tree, the global is_same variable 
will never get set to False and we will return True.

After solving this problem in the way described above, it could be noticed that the custom dfs function we defined has 
the same input parameters as the top level function.  This could be used as an indication that we could refactor our 
function to just use the top level function as our recursive function.  In doing that, our function still returns true 
or false, but it is not based off of a global variable.  This approach flips the logic from the last iteration where 
instead of stopping iteration in the case of an inequality in the tress, we switch to only continuing iteration if 
things are equal.  In this case, we switched from a negative stoppage approach to a positive continuation approach. 
'''

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      if not p and not q:
        return True
      if p and q and p.val == q.val:
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
      return False