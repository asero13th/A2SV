class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
      
        visited = set()
        initial = image[sr][sc]
        def inBound(x, y, grid):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
        def dfs(x, y):
            if (x, y) in visited:
                return 
           
            
            visited.add((x , y))
            
            if inBound(x, y, image) and image[x][y] == initial :
                dfs(x, y +1 )
                dfs(x + 1, y)
                dfs(x, y - 1)
                dfs(x - 1, y)

                image[x][y] = color
        dfs(sr, sc)
        return image
        