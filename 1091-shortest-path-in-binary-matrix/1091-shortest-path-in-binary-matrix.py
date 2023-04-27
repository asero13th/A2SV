class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        
        
                
        def bfs(node):
            if grid[0][0] != 0:
                return -1
            
            visited = set({(0,0)})
            queue = deque([node])
        
            
            while queue:
                
                x, y , z = queue.popleft()
               
                direction = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
                # print(x, y, z)
                if (x, y) ==  (len(grid) - 1, len(grid) - 1):
                    return z
                
               
                
                for i,j in direction:
                    
                    if x + i >= 0 and x + i < len(grid) and y + j >=0 and y + j <len(grid):
                        if grid[x + i][y + j] == 0 and (x + i, y + j) not in visited:
                            queue.append((x + i, y + j, z + 1))
                            visited.add((x + i ,y + j))
                           
                            
                        
                       
                # print(visited, queue)
                
            return -1
        return bfs((0, 0,1))
            
                    
                    
                
                    
                
                
                
        
                
        
        
        
        
        