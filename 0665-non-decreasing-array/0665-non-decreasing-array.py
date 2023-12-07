class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return nums[:i] + nums[i +1:] == sorted(nums[:i] + nums[i +1:]) or nums[:i - 1] + nums[i :] == sorted(nums[:i - 1] + nums[i :])
        return True
        