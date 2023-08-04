class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(idx, arr):
            if len(arr) == k:
                ans.append(arr.copy())
                return
            
            for i in range(idx + 1, n + 1):
                arr.append(i)
                backtrack(i,arr)
                arr.pop()
          
        backtrack(0, [])
        return ans