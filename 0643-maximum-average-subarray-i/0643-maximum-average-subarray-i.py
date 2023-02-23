class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = -1 * 10** 4 + 1
        prefix = 0
        left = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if i >= k - 1:
                ans = max(ans, prefix/k)
                prefix -= nums[left]
                left += 1
                
                
        return ans
            

                
        
        