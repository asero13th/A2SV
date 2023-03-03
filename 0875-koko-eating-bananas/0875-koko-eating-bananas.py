class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        
        while left <= right:
            middle = (left + right)//2
            
            if  not self.isValid(piles, middle, h):
                left = middle + 1
            elif middle != 1 and self.isValid(piles, middle, h) and self.isValid(piles, middle - 1,h):
                right = middle - 1
            else: return middle
    
    
    def isValid(self,piles, k,h):
        
        total = 0
        
        for pile in piles:
            total += ceil(pile/k)
        return total <= h
        