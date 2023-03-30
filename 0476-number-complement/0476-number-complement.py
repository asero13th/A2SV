class Solution:
    def findComplement(self, num: int) -> int:
        if num & num - 1 == 0:
            return num - 1
        
        n = 1<<(ceil(log(num,2)))
        return  (n - 1) ^ (num)
        