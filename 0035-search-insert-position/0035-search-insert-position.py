class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] > target: return 0
        if nums[len(nums) - 1] < target: return len(nums)
        left, right = 0, len(nums) - 1
        middle = (left + right)//2
        
        while left <= right:
            
            if nums[middle] < target: left = middle
            elif nums[middle] > target: right = middle
            elif nums[middle] == target: return middle
            
            middle = (left + right)//2
            
            if middle == left and nums[middle] == target: return left
            if middle == left: return left + 1
            if middle == right and nums[middle] == target: return right
            elif middle == right: return right
            
                
            

        