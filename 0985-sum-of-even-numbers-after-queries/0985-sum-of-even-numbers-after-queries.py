class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        evensum = sum(v for v in nums if v % 2 == 0)
        
        for val, idx in queries:
            num = nums[idx]
            if num % 2 == 0: evensum  -= num
                
            nums[idx] += val
            
            if nums[idx] % 2 == 0: evensum += nums[idx]
                
            ans.append(evensum)
            
        return ans