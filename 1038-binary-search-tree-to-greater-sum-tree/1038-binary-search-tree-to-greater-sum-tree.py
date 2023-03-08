# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def newTree(node, prefix):
            if node.right:
                prefix = newTree(node.right, prefix)
            
            node.val += prefix
            prefix  = node.val
            
            if node.left:
                prefix = newTree(node.left, prefix)
            
            return prefix
        
        newTree(root, 0)
        
        return root
        