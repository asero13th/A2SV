class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        var = 0
        for i in nums:
            var = var^i
        return var