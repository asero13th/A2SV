class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        perimeter = 0
        i,j,k = len(nums) - 1,len(nums) - 2,len(nums) - 3
        while k >= 0:
            if nums[i] < nums[j] + nums[k]:
                perimeter = max(perimeter,nums[i] + nums[j] + nums[k])
                
            i -= 1
            j -= 1
            k -= 1
        return perimeter
            