class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        if x == 0:
            return 0
        while left <= right:
            middle = (right + left)//2
            
            if middle * middle > x:
                right = middle  - 1
            elif middle * middle < x:
                left = middle + 1
            else:
                return middle
        return middle if middle * middle <= x else middle - 1    
        
                
                
            
        
        