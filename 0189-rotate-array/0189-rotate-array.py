class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = k % len(nums)
        tmp = []
        for i in range(len(nums) - n,len(nums)):
            tmp.append(nums[i])
            
        for i in range(len(nums) - n - 1,-1,-1):
            nums[i + n] = nums[i]
            
        for i in range(n):
            nums[i] = tmp[i]
            
        
        