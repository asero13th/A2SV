class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,j = 0,len(nums) - 1
        while i <= j:
            if nums[i] == val:
                num = nums.pop(i)
                nums.append(num)
                j -= 1
            else:
                i += 1
        return j + 1
            
        