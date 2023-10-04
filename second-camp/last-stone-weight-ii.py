class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        summ = sum(stones)
        target = ceil(summ / 2)
        
        memo = {}
        @cache
        def dp(i, total):
            nonlocal target
            if i == len(stones) or total >= target:
                return abs(total - (summ - total))
            
            
            ans1 = (dp(i + 1, total + stones[i]) )
            ans2 = (dp(i + 1, total))

            return min(ans1, ans2)
             
        return dp(0, 0)

        

        
        
