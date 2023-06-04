class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        dp = collections.defaultdict(int)
        ans = 1
        for n in arr:
            if n - difference in dp:
                dp[n] = max(dp[n], dp[n - difference] + 1)
                ans = max(ans, dp[n])
            elif n not in dp: dp[n] = 1
        return ans
               
        