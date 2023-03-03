class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def leftBound(nums, target):
            left, right = 0 , len(nums) - 1
            while left <= right:
                middle = (left + right )//2
                
                if nums[middle] < target:
                    left = middle + 1
                
                elif nums[middle] > target or (nums[middle] == target and middle > 0 and nums[middle - 1] == target):
                    right = middle - 1
                else:
                    if nums[middle] == target:
                        return middle
                    else: return -1
            return -1
        
        def rightBound(nums, target):
            left, right = 0 , len(nums) - 1
            while left <= right:
                middle = (left + right )//2
                
                if nums[middle] < target  or (nums[middle] == target and middle < len(nums) - 1 and nums[middle + 1] == target):
                    left = middle + 1
                
                elif nums[middle] > target:
                    right = middle - 1
                else:
                    if nums[middle] == target:
                        return middle
                    else: return -1
            return -1
                
        return [leftBound(nums, target), rightBound(nums, target)]
                
            
        