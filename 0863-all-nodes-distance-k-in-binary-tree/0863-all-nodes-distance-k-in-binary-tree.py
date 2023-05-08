# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        hashmap = defaultdict(list)
        def dfs(node):
            
            
            if not node:
                return 
            
            if node.right:
                hashmap[node.val].append(node.right.val)
                hashmap[node.right.val].append(node.val)
                
                
            if node.left:
                hashmap[node.val].append(node.left.val)
                hashmap[node.left.val].append(node.val)
            
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        def bfs(graph):
            
            queue = deque([target.val])
            visited = {target.val}
            level = 0
            while queue:
                
                if level  == k:
                    return list(queue)
                
                
                for i in range(len(queue)):
                    node =  queue.popleft()
                    
                    for val in graph[node]:
                        if val not in visited:
                            visited.add(val)
                            queue.append(val)
                if queue: 
                    level += 1 
            return []
        return bfs(hashmap)

                        

            
            
            
            
            
        
        
            
            
            
        