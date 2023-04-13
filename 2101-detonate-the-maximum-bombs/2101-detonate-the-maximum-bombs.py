class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def adjList(bombs):
            graph = defaultdict(list)
            n = len(bombs)
            
            for i in range(n):
                for j in range(n):
                    if(i==j):
                        continue

                    x1,y1,r1 = bombs[i]
                    x2,y2,r2 = bombs[j]

                    if(r1 >= math.sqrt((x2-x1)**2 + (y2-y1)**2)):
                        graph[i].append(j)
            return graph


        graph = adjList(bombs)
        
        
        def dfs(node):
            nonlocal visited
            
            for nei in graph[node]:
                if(nei not in visited):
                    visited.add(nei)
                    dfs(nei)
        
        
        ans = 0
        n = len(bombs)
        for i in range(n):
            visited = set([i])
            dfs(i)
            ans = max(ans,len(visited))
           
        return ans
        



                    
                    
            
        
         