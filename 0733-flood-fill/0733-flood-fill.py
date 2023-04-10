class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
      
        visited = set()
        
        def dfs(x, y):
            if (x, y) in visited:
                return 
            if x < 0 or x > len(image) - 1:
                return 
            
            if y < 0 or y > len(image[0])  - 1:
                return 
            
            visited.add((x , y))
            
            if image[x][y] == image[sr][sc]:
                dfs(x, y +1 )
                dfs(x + 1, y)
                dfs(x, y - 1)
                dfs(x - 1, y)

                image[x][y] = color
        dfs(sr, sc)
        return image
        