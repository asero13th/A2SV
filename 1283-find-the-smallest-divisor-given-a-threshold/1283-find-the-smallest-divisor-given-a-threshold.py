class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        maximum = max(nums)
        
        def checker(nums, target):
            ans = 0
            for num in nums:
                ans += (ceil(num/target))
            return ans
        
        left, right = 1, maximum
        while left <= right:
            middle = (left + right)//2
            if checker(nums, middle) > threshold:
                left = middle + 1
            else:
                right = middle - 1
        return left
        
        