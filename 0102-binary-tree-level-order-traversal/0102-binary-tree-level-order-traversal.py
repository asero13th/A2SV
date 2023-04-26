# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def bfs(node):
            if not node:
                return 
            queue = deque([node])
            
            while queue:
                tmp = []
                for node in queue:
                    tmp.append(node.val)
                ans.append(tmp.copy())
                
                for i in range(len(queue)):
                    node = queue.popleft()
                    
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                
        bfs(root)
        return ans
        
                    
                    
                
        
        