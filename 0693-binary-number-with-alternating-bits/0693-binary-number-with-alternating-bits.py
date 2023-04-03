class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        num = bin(n)
        for i in range(1,len(num)):
            if num[i] == num[i - 1]:
                return False
        return True
        
        