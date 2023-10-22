class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)

 
        if summ % 2 != 0:
            return False
        target = summ // 2
        ans = False
        
        @cache
        def dp(idx, total):
            nonlocal ans
            if idx >= len(nums) or total > target:
                return False
            
            if total == target:
                return True

            return dp(idx + 1, total) or dp(idx + 1, total + nums[idx])

        return dp(0, 0)