class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        dp[-1] = matrix[-1]
        def inBound(i , j):
            nonlocal n
            return 0 <= i < n and 0 <= j < n
            
        
        for i in range(n - 2, -1, -1):
            for j in range(n - 1, -1, -1):
                minimum = float("inf")
                if inBound(i + 1, j + 1):
                    minimum = min(dp[i + 1][j + 1], minimum)
                if inBound(i + 1, j - 1):
                    minimum = min(dp[i + 1][j - 1], minimum)
                if inBound(i + 1, j):
                    minimum = min(dp[i + 1][j], minimum)
                    
                dp[i][j] = matrix[i][j] + minimum
              
        return (min(dp[0]))
                
        