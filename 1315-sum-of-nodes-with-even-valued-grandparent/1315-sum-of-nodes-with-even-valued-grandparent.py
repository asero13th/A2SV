# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        arr = []
        def dfs(node, parent):
            if not node:
                return
            
            if parent % 2 == 0:
                if node.left:
                    arr.append(node.left.val)
                
                if node.right:
                    arr.append(node.right.val)
                    
            dfs(node.left, node.val)
            dfs(node.right, node.val)
        dfs(root, -1)
        return sum(arr) if arr else 0
            
        