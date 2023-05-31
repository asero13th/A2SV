class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        
        def dp(row, col):
            if row > m - 1 or col > n - 1:
                return 0
            
            if row  ==  m - 1 and col == n - 1:
                return 1
            
            if (row, col) not in memo:
                down = dp(row + 1, col)
                right = dp(row, col + 1)
       
                memo[(row, col)] = (down + right)
                return down + right
            return memo[(row, col)]
        
        return(dp(0,0))
            
                
                
        
        