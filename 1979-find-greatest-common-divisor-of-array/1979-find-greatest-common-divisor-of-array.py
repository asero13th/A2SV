class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minimum = min(nums)
        maximum = (max(nums))
        num = 1
        for i in range(1, minimum + 1):
            if minimum % i == 0 and maximum % i == 0:
                num = i
        return num
            
        