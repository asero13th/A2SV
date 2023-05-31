class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for i in range(n)] for _ in range(m)]
        memo[ -1][ - 1] = 1
        
        
        for i in range( m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i > 0:
                    memo[i - 1][j] += memo[i][j]
                if j > 0:
                    memo[i][j - 1] += memo[i][j]
        return memo[0][0]
                
        
        
        
        
        
        
            
                
                
        
        