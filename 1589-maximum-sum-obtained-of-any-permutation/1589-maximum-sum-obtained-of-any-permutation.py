class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr = [0] * len(nums)
        for left, right in requests:
            arr[left] += 1
            if right < len(arr) - 1: arr[right + 1] -= 1
        
        prefix = 0
        prefix = list(accumulate(arr))
        prefix.sort()
        nums.sort()
        ans = 0
        
        for i in range(len(nums)):
            ans += (nums[i] * prefix[i])
        return ans % (10**9 + 7)
        