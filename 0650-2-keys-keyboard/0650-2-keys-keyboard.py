class Solution:
    def minSteps(self, n: int) -> int:
        def isprime(n):
            if n == 1:
                return False
            for i in range(2, int(n**0.5) +1):
                if n % i == 0:
                    return i
            return n
        
        def solve(n):
            if n == 1: return 0
            x = isprime(n)
            
            if x == n:
                return x
            
            return x + solve(n//x)
        return solve(n  )    