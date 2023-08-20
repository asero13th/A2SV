class Solution:
    def reverse(self, x: int) -> int:

        n = abs(x)
        num = 0
        power = len(str(n)) - 1
        
        while n > 0:
            val = n % 10
            num = num + (val * (10**power))
            n = n // 10
            power -= 1
            
        if num < -2147483647 or num > 2147483647:
            return 0
        
        return num if x >= 0 else -num
            
            
        
        