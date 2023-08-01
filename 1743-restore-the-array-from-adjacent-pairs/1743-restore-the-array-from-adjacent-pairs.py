class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        def adjList():
            graph = defaultdict(list)
            degree = defaultdict(int)
            maximum = 0
            for u, v in adjacentPairs:
                graph[u].append(v)
                graph[v].append(u)
                degree[u] += 1
                degree[v] += 1
            
            return [degree, graph]
        degree, graph = adjList()
        ans = []
        
        queue = deque()
        tmp =  []
        for edge in degree:
            if degree[edge] == 1:
                tmp.append(edge)
               
        queue.append(tmp[0])
        
        while queue:
            
            node  = queue.popleft()
            ans.append(node)
            for neigh in graph[node]:
                degree[neigh] -= 1
                
                if degree[neigh] == 1:
                    queue.append(neigh)
        ans.append(tmp[1])
        return ans
                
        
        
        
        
            
        