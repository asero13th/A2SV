class Solution:
    def splitString(self, s: str) -> bool:
        
        def backtrack(index, parts, prev_val):
            if index == len(s):
                return parts >= 2
            
            for i in range(index, len(s)):
                num = int(s[index:i+1])
                
                if prev_val == math.inf or num == prev_val - 1:
                    if backtrack(i + 1, parts + 1, num):
                        return True
                                        
            return False
        return backtrack(0,0,math.inf)
        