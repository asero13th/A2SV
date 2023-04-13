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
        
#         def adjList(bombs):
#             hashmap = defaultdict(list)
#             for i, arr in enumerate(bombs):
                
#                 x, y, r = arr[0], arr[1], arr[2]
                
#                 for j, li in enumerate(bombs):
#                     k,l,m  = li[0], li[1], li[2]
#                     if  math.sqrt((x - k)**2 + (y - l)**2) <= r and  i != j:
#                         hashmap[j].append(i)
#                         hashmap[i].append(j)
#             return hashmap
        
#         adj = adjList(bombs)
#         visited = set()
#         def dfs(vertex, length):
            
            
#             visited.add(vertex)
#             for neigh in adj:
#                 if neigh not in visited:
#                     dfs(neigh, length)
#                     length += 1
                    
#             return length
                    
            
#         print(adj)
#         ans = 1
#         for val in adj:
#             if val not in visited:
#                 ans = max(ans, dfs(val, 0))            
#         return ans
                    
                    
            
        
         