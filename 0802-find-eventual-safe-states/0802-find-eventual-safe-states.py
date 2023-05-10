class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        def bfs(grid):
            
            graph = defaultdict(list)
            degree = defaultdict(int)
            queue = deque()
            
            for i, row in enumerate(grid):
                for j, val in enumerate(row):
                    degree[i] += 1
                    graph[val].append(i) 
                    
                if not row:
                    queue.append(i)
            ans = []
          
            while queue:
                
                node =  queue.popleft()
                ans.append(node)
                for neigh in graph[node]:
                    degree[neigh] -= 1
                        
                    if degree[neigh] == 0:
                        queue.append(neigh)
            return ans
        ans = bfs(graph)
        ans.sort()
        return ans
                    
                
            
            
            
        