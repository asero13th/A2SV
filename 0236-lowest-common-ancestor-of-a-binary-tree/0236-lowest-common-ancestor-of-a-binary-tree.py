# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def findRoot(node, p, q):
            if not node:
                return None
            
            if node.val == p.val or node.val == q.val:
                return node
            
            left  = findRoot(node.left, p, q)
            right  = findRoot(node.right, p ,q)
            
            if left and right:
                return node
            
            if left:
                return left
            
            else:
                return right
            
            
        return findRoot(root, p, q)
            
            
        
        