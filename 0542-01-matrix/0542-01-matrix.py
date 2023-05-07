class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
  
        def bfs(grid):
            ans = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
            queue = deque()
            visited = set()
            print(ans)
            for i, row in enumerate(mat):
                for j, num in enumerate(row):
                    if num  == 0:
                        queue.append((i,j))
                        visited.add((i, j))
                        ans[i][j] == 0
            
            
            level = 1
            while queue:
                
                for _ in range(len(queue)):
                    node = queue.popleft()
                    direction = [(1,0), (0,1), (-1,0), (0,-1)]
                    
                    for x, y in direction:
                        i, j = node[0], node[1]
                        if 0 <= (x + i) < len(grid) and 0 <= (y + j) < len(grid[0]) and (x + i, y + j) not in visited:
                            ans[x + i][y + j]  = level
                            queue.append((x + i, y + j))
                            visited.add((x + i, y + j))
                            
                level += 1
            return ans
        return bfs(mat)
        
                        
                        
                            
                            
                            
                            
                            
                            
                    
                    
                 
                    
                
                
                
                
                    
                
        