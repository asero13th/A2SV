class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        if amount == 0:
            return 0
        
        def dp(curr):
            if curr == 0:
                return 0
            
            if curr in memo:
                return memo[curr]
                
            ans = float("inf")
            for val in coins:
                if (curr  - val) >= 0:
                    ans = min(ans, dp(curr - val))
            
            memo[curr] = ans + 1
            return memo[curr]
        ans = dp(amount)
        return ans if ans != float("inf") else -1 
        