class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums) + 1
        prefix = 0
        left = 0
        for right, val in enumerate(nums):
            prefix += val
            while prefix >= target:
                ans = min(ans, right - left + 1)
                prefix -= nums[left]
                left += 1
                
        return ans if ans != len(nums) + 1 else 0
                