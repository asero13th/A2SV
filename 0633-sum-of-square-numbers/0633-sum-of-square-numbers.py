class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n  = int(sqrt(c))
        i,j = 0,n
        while i <= j:
            if i**2 + j**2 == c:
                return True
            elif i**2 + j**2 < c:
                i += 1
            else:
                j -= 1
        return False
            