class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        arr = []
        visited = set()
        answer = []
        
        def backtrack():
            if len(arr) == len(nums):
                answer.append(arr.copy())
                return
                
            
            for i in range(len(nums)):
                if nums[i] not in visited:
                    arr.append(nums[i])
                    visited.add(nums[i])
                    backtrack()
                    arr.pop()
                    visited.remove(nums[i])
        backtrack()
        return answer