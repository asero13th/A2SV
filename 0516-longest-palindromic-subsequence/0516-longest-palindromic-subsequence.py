class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
       
        @cache
        def dp(i, j):
            if i == j:
                return 1

            if i > j:
                return 0   
            ans = 0
            if s[i] == s[j]:
                ans = dp(i + 1, j - 1) + 2
            else:
                ans = max(dp(i + 1, j), dp(i, j -1))
            
            return ans
        return dp(0, len(s) - 1)
        