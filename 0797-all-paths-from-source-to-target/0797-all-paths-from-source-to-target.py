class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def adjecency(matrix):
            hashmap = defaultdict(list)
            for i, graph in enumerate(matrix):
                hashmap[i] = graph
                
            return hashmap
        
        adj = adjecency(graph)
        ans = []
   

        def dfs(vertex, tmp):
            tmp.append(vertex)
            
            if vertex == len(graph) - 1:
                ans.append(tmp.copy())
                return
             
      
            for neigh in adj[vertex]:
               
                dfs(neigh, tmp)
                tmp.pop()
                 
        dfs(0, [])
        return ans
                
            
            
        
        