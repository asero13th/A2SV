# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return 0
        
            left = helper(root.left) + 1
            right = helper(root.right) + 1

            if abs(left - right) > 1:
                return float("inf")

            return max(left, right)
        return True if helper(root) != float('inf') else False

        