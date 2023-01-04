class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans, evensum = [], 0
        for num in nums:
            if num % 2 == 0: evensum += num

        for val, idx in queries:
            num = nums[idx]
            if num % 2 == 0: evensum  -= num
                
            nums[idx] += val
            
            if nums[idx] % 2 == 0: evensum += nums[idx]
                
            ans.append(evensum)
            
        return ans