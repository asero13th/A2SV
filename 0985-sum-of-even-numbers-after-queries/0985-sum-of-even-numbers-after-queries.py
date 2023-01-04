class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans, evensum = [], 0
        for num in nums:
            if num % 2 == 0: evensum += num

        for val, idx in queries:
            num = nums[idx]
            if self.iseven(num):
                evensum  -= num
                
            nums[idx] += val
            if self.iseven(nums[idx]):
                evensum += nums[idx]
            ans.append(evensum)
            
        return ans
                
            
    def iseven(self, num):
        return num % 2 == 0
            