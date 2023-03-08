# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def collect(root):
            if not root:
                return []
            
            if not root.right and not root.left:
                return [[str(root.val)]]

            left = collect(root.left)
            right = collect(root.right)
            
            # print(left, right)
            
            if left:
                for arr in left: arr.insert(0, str(root.val))
                    
            if right:
                for arr in right: arr.insert(0, str(root.val))
            
            left.extend(right)
            return left
        
        ans = collect(root)
        for i, string in enumerate(ans):
            ans[i] = "->".join(string)
        return ans
                
                