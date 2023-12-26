class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        memo = {}
        @cache
        def count(left, target):
            if left == 0:
                if target == 0:
                    return 1
                else:
                    return 0
                
            if target < 0:
                return 0
            
            ways = 0
            for i in range(1, k + 1):
                ways += count(left - 1, target - i)
                ways %= MOD
                
            return ways
        return count(n, target)