class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        tot = nums[0]
        n = len(nums)
        i = 1
        ans = 0
        while n - i:
            tillNow = ceil(tot/i)
            tot += nums[i]
            i += 1
            current = ceil(tot/i)
            ans = max(tillNow, current, ans)
        return ans
        
        