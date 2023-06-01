class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 2:
            return max(nums)
        memo = {}
        n = len(nums)
        
        def dp(state, idx):
            if idx == n:
                return 0
            
            if (state, idx) not in memo:
                take = 0
                if state:
                    take = dp(False, idx + 1) + nums[idx]
                    
                not_take = dp(True, idx + 1)
                memo[(state, idx)] = max(take, not_take)
                
            return memo[(state, idx)]
      
        return dp(True, 0)
                
                