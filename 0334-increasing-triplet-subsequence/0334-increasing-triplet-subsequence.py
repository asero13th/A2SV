class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float('inf'), float('inf')
        for i, num in enumerate(nums):
            if num < first:
                first = num
            elif num < second and num > first:
                second = num
            elif num > second:
                return True
        return False