class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = {i:i for i in range(1,n + 1)}
        rank = {i:1 for i in range(1, n + 1)}
        
        
        def unioNfind(x):
            if graph[x] == x:
                return x
            
            val = unioNfind(graph[x])
            graph[x] = val
            return val
        
        def solve():
            
            for x, y in edges:
                edge1 = unioNfind(x)
                edge2 = unioNfind(y)
                
                if edge1 != edge2:
                    if rank[edge1] > rank[edge2]:
                        graph[edge2] = graph[edge1]
                        rank[edge1] += rank[edge2]
                        
                    else:
                        graph[edge1] = graph[edge2]
                        rank[edge2] += rank[edge1]
                else:
                    ans = [x, y]
            return  ans
        return solve()
     
        