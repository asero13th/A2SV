class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        count = Counter(nums)
        n = len(count)
        
        if n <= 2:
            return -1
        
        return nums[-2]