class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        
        nums.sort()
        hashmap = {
            0: len(nums) - 4,
            1: len(nums) - 3,
            2: len(nums) - 2,
            3: len(nums) - 1
    
        }
        
        ans = nums[-1] - nums[0]
        
        for key, val in hashmap.items():
            ans = min(ans, nums[val] - nums[key])
        return ans
        
        
        