# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def getRoot(left, right):
            if right < left:
                return None
            
            middle = (left + right) // 2
            root = TreeNode(nums[middle])
            
            root.right = getRoot(middle+1, right)
            root.left = getRoot(left, middle - 1)
            
            return root
        
        return getRoot(0, len(nums)-1)
            
        
            
            
        
        