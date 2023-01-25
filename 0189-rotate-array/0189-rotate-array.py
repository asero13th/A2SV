class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        l,r = 0,len(nums) -1
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1
        ll,rl = 0,k  - 1
        lr,rr = k,len(nums) - 1
        while ll < rl:
            nums[ll],nums[rl] = nums[rl],nums[ll]
            ll += 1
            rl -= 1
        while lr < rr:
            nums[lr],nums[rr] = nums[rr],nums[lr]
            lr += 1
            rr -= 1