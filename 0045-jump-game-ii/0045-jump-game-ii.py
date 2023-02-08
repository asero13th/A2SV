class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = [float("inf") for _ in range(len(nums))]
        memo[0] = 0
        n = len(nums)-1
        for i in range(len(nums)):
            for j in range(i+1,i+nums[i]+1):
                if j >= len(memo):break
                elif memo[j] > memo[i]+1:
                    memo[j] = memo[i] + 1
        return memo[n]
        