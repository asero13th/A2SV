# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(nums):
            if not nums:
                return 

            if len(nums) == 1:
                return TreeNode(nums[0])
            
            middle = (len(nums) - 1)//2
            ans = TreeNode(nums[middle]) 
            
            ans.left = helper(nums[:middle])
            ans.right = helper(nums[middle + 1:])
            
            return ans
        return helper(nums)