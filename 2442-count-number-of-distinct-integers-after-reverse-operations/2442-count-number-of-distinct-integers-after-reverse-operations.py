class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        numset = set(nums)
        
        for num in nums:
            numset.add(int("".join(reversed(str(num)))))
        return len(numset)
        