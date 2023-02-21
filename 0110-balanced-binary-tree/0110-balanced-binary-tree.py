# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return False if self.checker(root) ==  float('inf') else True
        
    def checker(self,root):
        if not root:
            return 0
        
        left  = self.checker(root.left)
        right = self.checker(root.right)
        
        if abs(left - right) > 1:
            return float('inf')
        
        return max(left, right) + 1
            
        
        