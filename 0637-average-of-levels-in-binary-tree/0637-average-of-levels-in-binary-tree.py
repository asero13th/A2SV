# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        
        def bfs(node):
            queue = deque([node])
            
            
            while queue:
                total = 0
                length = len(queue)
                
                for i in range(length):
                    
                    node = queue.popleft()
                    total += node.val
                    
                    if node.left:
                        queue.append(node.left)
                        
                    if node.right:
                        queue.append(node.right)
                        
                ans.append(total/ length)
            return ans
        return bfs(root)
                    
                    
                    
                    
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        

#         def bfs(node):
        
#             queue = deque([node])
           
#             while queue:
#                 total = 0
#                 len_queue = len(queue)
                
#                 for i in range(len(queue)):
#                     node = queue.popleft()
#                     total = total + node.val
                    
#                     if node.left:
#                         queue.append(node.left)

#                     if node.right:
#                         queue.append(node.right)
                
                    
#                 average = total / len_queue 
#                 ans.append((average))
               
#         bfs(root)
#         return ans        