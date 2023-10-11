class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        target = 0
        curr = 0
        
        if len(haystack) < n:
            return -1 
        
        for i in range(n):
            target += ((ord(needle[i]) - ord('a')) * pow(26, n - i - 1))        
            curr += ((ord(haystack[i]) - ord('a')) * pow(26, n - i - 1))
        
        
        
        left = 0
        right = n 
        
        while right < len(haystack):
            if curr == target: 
                return left
            
            curr -= ((ord(haystack[left]) - ord('a')) * pow(26, n - 1))
            curr = curr * 26
            
            curr += (ord(haystack[right]) - ord('a'))
             
            left += 1
            right += 1
            
            
            
        if target == curr:
            return left
              
               
               
        return -1