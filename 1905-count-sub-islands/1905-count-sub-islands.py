class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        
        def adj(grid1, grid2):
            ans = [[],[]]
            for i in range(len(grid1)):
                for j in range(len(grid1[i])):
                    if grid1[i][j] == 1:
                        ans[0].append((i,j))
                        
                    if grid2[i][j] == 1:
                        ans[1].append((i,j))
            return ans
        
        graph1, graph2 = adj(grid1, grid2)
       
                    
        def dfs(x, y):
            nonlocal tmp
         
            
            if x < 0 or x > len(grid1) - 1:
                return
            
            if  y < 0 or y > len(grid1[0]) - 1:
                return 
            
            if grid2[x][y] != 1:
                return 
            if ((x, y)) not in visited:
                visited.add((x, y))
                tmp.add((x , y))

                dfs(x + 1, y)
                dfs(x ,y - 1)
                dfs(x - 1, y)
                dfs(x, y + 1)
            
        
                
                        
        def subisland(g1, g2):
            for i, j in g1:
                if  g2[i][j] != 1:
                    return 0
            return 1
        
        ans = 0
        for x , y in graph2:
            tmp = set()
            if (x,y) not in visited:
               
                dfs(x, y)
                ans += subisland(tmp, grid1)
    
        return ans
                        
                    
                
                
            
        