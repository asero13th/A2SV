# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        def bfs(node):
            if not node:
                return []
            
            queue = deque([(node, 0)])
            hashmap = defaultdict(list)
            while queue:
                
                node, idx = queue.popleft()
                hashmap[idx].append(node.val)
                if node.left:
                    queue.append((node.left, idx + 1))
                    
                if node.right:
                    queue.append((node.right, idx + 1))
                
            ans = []
            for item in sorted(hashmap.keys(), reverse = True):
                ans.append(hashmap[item])
            return ans
                
        return bfs(root)
                    
            
            
        