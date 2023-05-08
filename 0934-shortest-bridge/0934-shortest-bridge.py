class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(r, c) :
            if grid[r][c] == 1 :
                q.append((r, c, 0))
                grid[r][c] = '$'
                if r-1 >= 0 : dfs(r-1, c)
                if r+1 < len(grid) : dfs(r+1, c)
                if c-1 >= 0 : dfs(r, c-1)
                if c+1 < len(grid) : dfs(r, c+1)
        
        def bfs(q) :
            seen = set()
            while q :
                i, j, d = q.popleft()
                if grid[i][j] == 1 :
                    return d
                else :
                    for x, y in ((i-1, j), (i, j-1), (i+1, j), (i, j+1)) :
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) : 
                            if (x, y) not in seen :
                                seen.add((x, y))
                                q.append((x, y, d+1))
        
        q = deque()
        flag = False
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == 1 :
                    dfs(i, j)
                    flag = True
                    break
            if flag :
                break
        
        return bfs(q) - 1
#         def getFirstOne(grid):
#             for i,row in enumerate(grid):
#                 for j, val in enumerate(row):
#                     if val == 1:
#                         return [i,j]
        
#         def getSet(i, j):
#             n,m = len(grid), len(grid[0])
        
#             queue = deque([(i,j)])
#             visited = set()
#             direction = [(0,1),(1,0),(0,-1),(-1,0)]
#             while queue:
                
#                 node = queue.popleft()
#                 visited.add(node)
#                 for x, y  in direction:
#                     if 0<=x+i<n and 0<=y+j<m and grid[x+i][y+j] == 1:
#                         queue.append(x+i, y+j)
#             return visited
                    
            
#         def bfs(grid):
#             n,m = len(grid), len(grid[0])
#             queue = deque()
#             i, j = getFirstOne(grid)
#             set1 = getSet(i, j)
            
            
#             for i,row in enumerate(grid):
#                 for j, val in enumerate(row):
#                     if ((i,j)) not in set1 and grid[i][j] == 1:
#                         queue.append(i,j)
            
#             visited = set()
#             direction = [(0,1),(1,0),(0,-1),(-1,0)]
#             while queue:
                
#                 level = 0
#                 for _ in range(len(queue)):
#                     i, j = queue.popleft()
                    
#                     for x, y in direction:
#                         if 0<=x+i<n and 0<=y+j<m and grid[x+i][y+j] not in set1:
#                             queue.append(x+i, y+j)
                            
                        
                        
                        
                        
                        
            
            
            
            
            
            
#         return bfs(grid)
                        
                