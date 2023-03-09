class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def helper(i, arr):
            if len(arr) == k:
                ans.append(arr)
                return
            
            for j in range(i + 1 , n + 1):
                helper(j , arr + [j])
                
            
        helper(0,[])
        return ans
                
                
        