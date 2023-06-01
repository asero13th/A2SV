class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        n = len(nums)
        
        def dp(summ, idx):
            if idx >= n:
                if summ == target:
                    return 1
                else:
                    return 0
                
            if (idx, summ) not in memo:
                left =  dp(summ + nums[idx], idx + 1)
                right =  dp(summ -  nums[idx] , idx + 1)
                
                
                memo[(idx, summ)] = left + right
            return memo[(idx, summ)]
                
            
        return dp(0,0)
                
            
            
                
        
        