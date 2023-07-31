class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        n = len(quiet)
        graph = defaultdict(list)
        indegree = [0] * n
        queue = deque()
        
        ans = [i for i in range(n)]
        
        for u, v in richer:
            graph[u].append(v)
            indegree[v] += 1
            
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            u = queue.popleft()
            mini = quiet[u]
            
            
            for v in graph[u]:
                if mini < quiet[v]:
                    
                    quiet[v] = mini
                    ans[v] = ans[u]
                indegree[v] -= 1
                
                if indegree[v] == 0:
                    queue.append(v)
        return ans
            
            
            