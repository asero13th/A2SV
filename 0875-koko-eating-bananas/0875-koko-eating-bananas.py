class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        
        answer = None
        while left <= right:
            middle = (left + right)//2
            
            result = self.isValid(piles, middle, h)
            if  not result:
                left = middle + 1
            else:
                answer = middle
                right = middle - 1 
        return answer
    
    def isValid(self,piles, k,h):
        
        total = 0
        
        for pile in piles:
            total += ceil(pile/k)
        return total <= h
        