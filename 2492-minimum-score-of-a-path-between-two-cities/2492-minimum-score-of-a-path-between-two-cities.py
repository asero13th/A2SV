class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(int)
        rank = defaultdict(int)
        for x, y, d in (roads):
            graph[x] = x
            graph[y] = y
            rank[x] = 1
            rank[y] = 1
            
            
        
        def unionFind(x):
            if graph[x] == x:
                return x
            
            val = unionFind(graph[x])
            graph[x] = val
            return val
        def solve(edges):
            
            for x, y, d in edges:
                edge1 = unionFind(x)
                edge2 = unionFind(y)
                
                if edge1 != edge2:
                    if rank[edge1] > rank[edge2]:
                        graph[edge2] = graph[edge1]
                        rank[edge1] += rank[edge2]
                        
                    else:
                        graph[edge1] = graph[edge2]
                        rank[edge2] += rank[edge1]
                
            ans = 10 ** 5
            for x, y, d in edges:
                if unionFind(x) == unionFind(y) == unionFind(1):
                    ans = min(ans, d)
            return ans
        
        return solve(roads)