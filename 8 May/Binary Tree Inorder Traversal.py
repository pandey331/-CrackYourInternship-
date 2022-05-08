class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
      #  l=self.inorderTraversal(root.left)
       # r=self.inorderTraversal(root.right)
    
        return self.inorderTraversal(root.left)+ [root.val] +self.inorderTraversal(root.right)
    
          
