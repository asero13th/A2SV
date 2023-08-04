class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(idx, arr, summ):
            if summ == target:
                ans.append(arr.copy())
                return
            if summ > target:
                return
            
            
            for i in range(idx, len(candidates)):
                arr.append(candidates[i])
                summ += candidates[i]
                backtrack(i, arr, summ)
                
                summ -= arr.pop()
                
        backtrack(0,[], 0)
        return ans
                
                
        