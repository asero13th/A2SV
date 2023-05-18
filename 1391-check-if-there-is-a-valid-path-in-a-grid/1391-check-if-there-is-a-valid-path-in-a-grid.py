class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        graph = {(i, j): (i, j) for i in range(len(grid)) for j in range(len(grid[0]))}
        rank = {(i, j): 1 for i in range(len(grid)) for j in range(len(grid[0]))}
        dictinary = {
            1 : [[1, 3, 5,],[]],
            2 : [[], [2, 5, 6]],
            3 : [[],[2, 5,6]],
            4 : [[1,3,5],[6,5,2]],
            5 : [[],[]],
            6 : [[5,1,3],[]]
        }
        
        def unionFind(x):
            if graph[x] == x:
                return x
            
            val = unionFind(graph[x])
            graph[x] = val
            return val
        
        def solve():

            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    
                    cur = unionFind((i, j))
                    right = (i, j)
                    bottom = (i, j)
                    cur_val = grid[i][j]
                    right_val = grid[i][j]
                    bottom_val = grid[i][j]
                    
                    if j < len(grid[0]) - 1:
                        right = unionFind((i, j + 1))
                        right_val = grid[i][j + 1]
                    if i < len(grid) - 1:
                        bottom = unionFind((i + 1, j))
                        bottom_val = grid[i + 1][j]
                        
                    if cur != right:
                        if right_val in dictinary[cur_val][0]:
                            if rank[cur] > rank[right]:
                                graph[cur] = graph[right]
                                rank[right] += rank[cur]
                            else:
                                graph[right] = graph[cur]
                                rank[cur] += rank[right]
                                
                                
                    if cur != bottom:
                        if bottom_val in dictinary[cur_val][1]:
                            if rank[cur] > rank[bottom]:
                                graph[cur] = graph[bottom]
                                rank[bottom] += rank[cur]   
                            else:
                                graph[bottom] = graph[cur]
                                rank[cur] += rank[bottom]
                                

           
            return unionFind((0,0)) == unionFind((len(grid) - 1, len(grid[0]) - 1))
        return solve()
            
        
                        
                        

        
        
        
        