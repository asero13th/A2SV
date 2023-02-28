class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        var1 = self.fib(n - 1)
        var2 = self.fib(n - 2)
        
        return var1 + var2