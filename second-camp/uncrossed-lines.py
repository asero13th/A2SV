class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[0 for i in range(n + 1)] for _ in range(m + 1)]
        print(dp)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if nums1[j] != nums2[i]:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
                else:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
        
        
        return dp[0][0]