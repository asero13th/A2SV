class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def helper(i, arr):
            if len(arr) == k:
                ans.append(arr.copy())
                return
            
            for j in range(i + 1 , n + 1):
                arr.append(j)
                helper(j , arr)
                arr.pop()
                
            
        helper(0,[])
        return ans
                
                
        