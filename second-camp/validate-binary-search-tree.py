# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, maximum):
            if not node:
                return True, maximum
            
            flag, maximum = check(node.left, maximum)
            
            if not flag or node.val <= maximum:
                return False, maximum
            
            maximum = node.val
            
            flag, maximum = check(node.right, maximum)    
            
            return flag, maximum
        flag, maximum = check(root, float("-inf"))
        return flag