class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numsCount = Counter(nums)
        for val in numsCount:
            if numsCount[val] == 1:
                return val
        