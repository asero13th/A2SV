class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodpair = 0
        nums.sort()
        i = 0
        while i < len(nums):
            if nums.count(nums[i]) > 1:
                goodpair += ((nums.count(nums[i]) * (nums.count(nums[i]) - 1))//2)
                i += nums.count(nums[i])
            else:
                i += 1
        return goodpair
        