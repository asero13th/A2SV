class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix, n = 1, 1, len(nums)
        ans = [1]
        
        for i in range(1,n):
            prefix *= nums[i - 1]
            ans.append(prefix)
        
        
        for i in range(n - 2, -1, -1):
            postfix *= nums[i + 1]
            ans[i] *= postfix
            
        return ans