# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        def solve(node):
            queue = deque()
            queue.append(node)
            
            ans = []
            
            while queue:
                length = len(queue)
                tmp = -2147483648
                
                for i in range(length):
                    node = queue.popleft()
                    tmp = max(tmp, node.val)
                    
                    if node.right:
                        queue.append(node.right)
                        
                    if node.left:
                        queue.append(node.left)
                    
                ans.append(tmp)
     
            return ans
        return solve(root)
            
                    
            
        