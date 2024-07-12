class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
      if not subRoot:
        return True
      if not root:
        return False

      def areSameTrees(root,subRoot):
        if not root and not subRoot:
          return True
        if root and subRoot and root.val == subRoot.val:
          return areSameTrees(root.left,subRoot.left) and areSameTrees(root.right,subRoot.right)
        return False

      if areSameTrees(root,subRoot):
        return True
      return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)