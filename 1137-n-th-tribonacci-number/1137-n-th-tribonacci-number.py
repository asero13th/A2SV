class Solution:
    def tribonacci(self, n: int) -> int:
        hashmap = {}
        def dp(n):
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            
            if n not in hashmap:
                hashmap[n] = dp(n - 1) + dp(n - 2) + dp(n - 3)
                
            return hashmap[n]

        return dp(n)
#         arr = [0] * 38
#         arr[0], arr[1], arr[2] = 0, 1, 1
        
#         for i in range(3,len(arr)):
#             arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
#         return arr[n]
    
        