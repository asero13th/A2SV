class Solution:
    def numTrees(self, n: int) -> int:
        dp = collections.defaultdict(lambda: 0)
        def helper(low, high):
            if low >= high:
                return 1
            pair = (low, high)
            if pair in dp:
                return dp[pair]
            for i in range(low, high + 1):
                dp[pair] += helper(low, i - 1) * helper(i + 1, high)
            return dp[pair]
        return helper(1, n)