class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backTrack(i, arr, target):
            if target == 0 and len(arr) == k:
                ans.append(arr.copy())
            
            if target <= 0 or len(arr) > k:
                return 
            
            for j in range(i, 10):
                backTrack(j + 1, arr + [j], target - j)
                
            
        backTrack(1, [], n)
        return ans
                

        