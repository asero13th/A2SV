# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root, array):
            if not root:
                return
            
            traverse(root.left,array)
            array.append(root.val)
            traverse(root.right,array)
            
            return array
            
        return traverse(root,[])
        
        
        
        