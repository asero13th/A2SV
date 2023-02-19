# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root,root)
        
        
        
    def isMirror(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        val1 = self.isMirror(p.right,q.left)
        val2 = self.isMirror(q.left,p.right)
        
        return val1 and val2
        
        
        
        
        
   