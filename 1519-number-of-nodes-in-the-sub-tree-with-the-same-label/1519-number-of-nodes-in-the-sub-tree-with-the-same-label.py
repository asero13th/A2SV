class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        counter = defaultdict(lambda: 0)
        graph = defaultdict(list)
        visited = [0] * n
        ans = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        
        def dfs(u):
            if visited[u]: return 

            visited[u] = 1
            counter[labels[u]] += 1
            start = maximum = counter[labels[u]]
            for v in graph[u]:
                dfs(v)
                maximum = max(maximum, counter[labels[u]])
            ans[u] = maximum-start+1

        dfs(0)
        return ans
            
        
            