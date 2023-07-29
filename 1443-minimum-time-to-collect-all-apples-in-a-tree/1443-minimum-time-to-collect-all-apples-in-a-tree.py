class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        count = hasApple.count(True)
        def adjList():
            
            graph  = defaultdict(list)
            for x, y in edges:
                graph[x].append(y)
                graph[y].append(x)
            return graph
        graph = adjList()
       
        def dfs(parent, vertex):
       
            count = 0
            
            for child in graph[vertex]:
                if child != parent:
                    count += dfs(vertex, child)
             
            if count:
                return count + 2 if vertex else count
            
            if hasApple[vertex] and vertex:
                return 2
            
            return 0
        
        return dfs(None,0)
                
     
            
            
             