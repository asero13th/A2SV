class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = k % len(nums)
        for i in range(n):
            nums.insert(0,nums.pop())
        
        