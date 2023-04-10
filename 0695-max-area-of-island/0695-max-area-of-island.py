class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def catchOnes(matrix):
            array = set()
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 1:
                        array.add((i, j))
            return array 
        Area = 0
        
        def dfs( grid, i, j):
            # conditions for out of bound and when we encounter water
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != 1:
                return 0

            maxArea = 1
            grid[i][j] = '#'  # this will act as visited set
            maxArea += dfs(grid, i+1, j)
            maxArea += dfs(grid, i-1, j)
            maxArea += dfs(grid, i, j+1)
            maxArea += dfs(grid, i, j-1)

            return maxArea
        if not grid:
            return 0
        ones = catchOnes(grid)
        
        
        for (x, y) in ones:
            Area = max(Area, dfs(grid, x, y))
            
        return Area
            
        
        
        
                         
                        
        