# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def helper(root1, root2):
            if not root1 and not root2:
                return 
            
            if root1 and  not root2:
                ans = TreeNode(root1.val)
                ans.left = helper(root1.left, None)
                ans.right = helper(root1.right,None)
                
            elif root2 and not root1:
                ans = TreeNode(root2.val)
                ans.left = helper(None,root2.left)
                ans.right = helper(None,root2.right)
            
            else:
                ans = TreeNode(root1.val + root2.val)
                ans.left = helper(root1.left, root2.left)
                ans.right = helper(root1.right, root2.right)
            return ans
        return helper(root1, root2)
        
        