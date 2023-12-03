class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        ans = []
        def dp(status, idx):
            if idx >= len(prices):
                return 0
            
            
            if (status, idx) in memo:
                return memo[(status, idx)]
            
            sum = 0
            if status:
                sum = max(dp(False, idx + 1) - prices[idx], dp(True, idx + 1))
                
            else:
                sum = max(dp(False, idx + 1), dp(True, idx + 1) + prices[idx] - fee)
                
            memo[(status, idx)] = sum
            return memo[(status, idx)]
        return dp(True, 0)
                
            
            
            
        