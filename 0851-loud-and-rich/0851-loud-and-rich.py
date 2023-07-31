class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        def adjList():
            graph = defaultdict(list)
            degree = defaultdict(int)
            for a, b in richer:
                graph[b].append(a)
                degree[a] = quiet[a]
            return [graph, degree]
        graph, degree = adjList()
        
        def dfs(vertex):
            nonlocal minimum
            if quiet[minimum] >= quiet[vertex]:
                    minimum = vertex
                    
            for neigh in graph[vertex]:
                
                    
                if neigh not in visited:
                    visited.add(neigh)
                    dfs(neigh)
            return minimum
        ans = []
        
        for i in range(len(quiet)):
            minimum = i
            visited = set()
            mini = dfs(i)
            ans.append(mini)
        return ans
            
        
        
                
                
        