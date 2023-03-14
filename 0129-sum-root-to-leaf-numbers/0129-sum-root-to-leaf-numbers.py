# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        def pathes(node, arr):
            nonlocal ans
            if not node:
                return
            
            if not node.right and not node.left:
                ans.append(arr)
           
            arr.append(str(node.val))
            
            pathes(node.left,arr.copy())
            pathes(node.right,arr.copy())
            
       
            return
        pathes(root,[])
        answer = 0
        for arr in ans:
            answer += int("".join(arr))
        return answer
        
            
        
        