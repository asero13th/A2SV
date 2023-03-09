# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        maximum = max(p.val,q.val)
        minimum = min(p.val,q.val)
        def checker(root, p, q):
            if root:
                if root.val > q:
                    return checker(root.left, p , q)
                elif root.val < p:
                    return checker(root.right, p, q)
                else:
                    return root
        return checker(root, minimum, maximum)
            
        
            
        
        