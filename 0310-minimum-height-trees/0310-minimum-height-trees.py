class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        def adjList():
            graph = defaultdict(list)
            degree = defaultdict(int)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
                degree[u] += 1
                degree[v] += 1
            return [graph, degree]
        
        graph, degree = adjList()
        queue = deque()
        
        for val in graph:
            if len(graph[val]) == 1:
                queue.append(val)
        def bfs():
            curr = n
            
            while curr > 2:
                size  = len(queue)
                curr = curr - size
                
                for i in range(size):
                    node = queue.popleft()
                    
                    
                    for neigh in graph[node]:
                        degree[neigh] -= 1
                        
                        if degree[neigh] == 1:
                            queue.append(neigh)
                    
                    
                    
                    
            return queue
        return bfs()
       

        
        