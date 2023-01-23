class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num_counter = [0]*len(nums)
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[j] < nums[i]:
                     num_counter[i] += 1
        return num_counter 
 