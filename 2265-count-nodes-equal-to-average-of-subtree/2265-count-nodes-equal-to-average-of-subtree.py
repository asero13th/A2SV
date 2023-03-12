# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        def findPreFix(node):
            nonlocal count
            if not node:
                return 0, 0
            
            left, lefttrees = findPreFix(node.left)
            right, righttrees = findPreFix(node.right)
        
            if  node.val == (right +  left + node.val)//(lefttrees + righttrees + 1):
                count += 1
            
            righttrees += 1
            
            return (right + left + node.val, lefttrees + righttrees)
        findPreFix(root)
        return count
        
            
            
            
        