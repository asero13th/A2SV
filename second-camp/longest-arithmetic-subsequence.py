class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        for i in range(len(nums)):
            for j in range(0, i):
                diff = nums[i] - nums[j]
                dp[(i, diff)] = dp[(j, diff)] + 1
        return max(dp.values()) + 1