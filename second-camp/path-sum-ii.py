# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        tmp = root
        if not root:
            return []
        tmparr = []
        ans = []
        def dfs(node, arr, summ):
            if not node:
                return

            summ +=  node.val
            arr.append(node.val)
            if not node.left and not node.right:
                if summ == targetSum:
                    ans.append(arr.copy())
                
            
            dfs (node.left, arr , summ)
            dfs (node.right, arr,summ)

            summ -= arr.pop()
      
        dfs(tmp, [], 0)
        print(ans)
        return ans
        





