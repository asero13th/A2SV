class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        def adjList(edges):
            graph = defaultdict(list)
            for i, j in edges:
                graph[j].append(i)
            return graph
        graph = adjList(edges)
        return [i for i in range(n) if i not in graph]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def adjecencyList(matrix):
#             occupied = [0] * n
#             hashmap = defaultdict(list)
#             for key, val in matrix:
#                 occupied[val] = 1
#             return occupied
#         ans = adjecencyList(edges)
      
#         return [i for i,val in enumerate(ans) if val == 0 ]
        