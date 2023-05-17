class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {i:i for i in range(n)}
        rank = {i:1 for i in range(n)}
        
        
        def unioNfind(x):
            if graph[x] == x:
                return x
            
            val = unioNfind(graph[x])
            graph[x] = val
            return val
        
        def solve(source, destination):
            
            for x, y in edges:
                edge1 = unioNfind(x)
                edge2 = unioNfind(y)
                
                if edge1 != edge2:
                    if rank[edge1] > rank[edge2]:
                        graph[edge2] = graph[edge1]
                        rank[edge2] += rank[edge1]
                        
                    else:
                        graph[edge1] = graph[edge2]
                        rank[edge1] += rank[edge2]
            return unioNfind(graph[source]) == unioNfind(graph[destination])
        return solve(source, destination)
     
            
        