class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        
        count = list(Counter(nums))
        count.sort()
        n = len(count)
        print(count)
        if n >= 3:
            return count[n - 3 ]
        return count[-1]
        