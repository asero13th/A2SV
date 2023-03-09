class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def helper(i, arr):
            if len(arr) == k:
                ans.append(arr)
                return
            
            for j in range(i , n + 1):
                helper(j + 1 , arr + [j])
                
            
        helper(1,[])
        return ans
                
                
        