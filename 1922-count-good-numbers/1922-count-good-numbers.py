class Solution:
    def countGoodNumbers(self, n: int) -> int:
        modulo  = 10 **9 + 7
        
        even = n//2 if n % 2 == 0 else n // 2 +1
        odd = n //2
        
        return (pow(5, even, modulo) * pow(4, odd, modulo)) % modulo
       
#         j= n//2
#         if n ==1:
#             return 5
#         elif n %2 ==0:
#             return ((5**j)% (10**9 +7))*(4**j % (10**9 +7))
        
#         else:
#             return ((5**(j+1) % (10**9 +7))*(4**j) % (10**9 +7))
    