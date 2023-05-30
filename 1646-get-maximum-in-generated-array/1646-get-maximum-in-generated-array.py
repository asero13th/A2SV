class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
      
        dp = [0]*(n+1)
        dp[0], dp[1] = 0, 1
      
        for i in range((n+1)//2):
            dp[2*i] = dp[i]
            dp[(2*i)+1] = dp[i] +dp[i+1] 
      
        return max(dp)
        