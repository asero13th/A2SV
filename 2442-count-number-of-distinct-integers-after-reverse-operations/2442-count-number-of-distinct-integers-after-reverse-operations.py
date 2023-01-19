class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        numset = set(nums)
        
        for num in nums:
            numset.add(int(str(num)[::-1]))
        return len(numset)
        