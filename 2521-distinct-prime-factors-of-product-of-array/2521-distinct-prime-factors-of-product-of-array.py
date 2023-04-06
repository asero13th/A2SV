class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        numset  = set()
        
        for num in nums:
            
            i = 2
            while num > 1:
                if num % i == 0:
                    numset.add(i)
                    num //= i
                else:
                    i += 1
        return len(numset)
        
        
        
        