class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        def backtrack(index, arr, nums):
            if len(arr) >= 2:
                answer.append(tuple(arr))
                
            
            for i in range(index, len(nums)):
                num = nums[i]
                if arr and arr[-1] > num:
                    continue
                arr.append(num)
                backtrack(i + 1, arr, nums)
                
                arr.pop()
        backtrack(0, [], nums)
        return set(answer)
                
                
        