# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(root):
            if not root:
                return ''
     
            return str(root.val) + '(' + dfs(root.left) + ')' + '(' + dfs(root.right) + ')'
        tt = dfs(root)
        tt = tt.replace('()()', '')
        tt = tt.replace(')()', ')')
        return tt
            
            
        
        