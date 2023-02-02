class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counted = Counter(nums)
        i,j = 0, len(nums) - 1
        for num in counted:
            while counted[num] > 2:
                j -= 1
                counted[num] -= 1
            for _ in range(counted[num]):
                nums[i] = num
                i += 1
        return j + 1
            
            
                
            
        