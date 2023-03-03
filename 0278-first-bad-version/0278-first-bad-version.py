# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left <= right:
            middle  = (left + right)//2
            if not isBadVersion(middle):
                left = middle + 1
            elif isBadVersion(middle) and isBadVersion(middle - 1):
                right = middle - 1
            else:
                return middle

                    
        
        