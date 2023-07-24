class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def onBoarder(x, y, grid):
            return (x == 0 or x == len(grid) - 1) or (y == 0 or y == len(grid[0]) - 1)
        
        def inBound(x, y, grid):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
        unCaptured = set()
        visited = set()
        for i in range(len(board)):
            for j  in range(len(board[0])):
                if onBoarder(i, j, board) and board[i][j] != "X":
                    unCaptured.add((i, j))
        
        def dfs(i, j):
            direction = [(0,1),(1,0),(0,-1),(-1, 0)]
            
            for x, y in direction:
                if inBound(x + i, y + j, board) and board[x + i][y + j] != "X" and (x + i, y + j) not in visited:
                    visited.add((x + i, y + j))
                    dfs(x + i, y + j)
                    
        for i, j in unCaptured:
            if (i, j) not in visited:
                dfs(i, j)
       
        for i in range(len(board)):
            for j  in range(len(board[0])):
                if (i, j) not in visited and (i, j) not in unCaptured:
                    board[i][j] = "X"
            
        
        
                    
                        
                    
        
                
            
        