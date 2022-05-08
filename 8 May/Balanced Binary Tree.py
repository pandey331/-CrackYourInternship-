class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #if not root:
         #   return true
        def traversal(node):
            if node is None:
                return 0
            left =traversal(node.left)
            right=traversal(node.right)
            level=max(abs(left),abs(right)) + 1
            
            if left < 0 or right < 0 or abs(left-right) > 1:
                return-1
            return level
        return traversal(root) >=0 
       
