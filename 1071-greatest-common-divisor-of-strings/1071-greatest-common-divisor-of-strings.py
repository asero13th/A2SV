class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        short = min(len(str1), len(str2))
        ans = ''
        real_ans = ''
        for i in range(short):
            if str1[i] == str2[i]:
                ans += str1[i]
                if ans * str1.count(ans) == str1 and ans * str2.count(ans) == str2:
                    real_ans = ans
            else:
                return ""
        return real_ans
        
        
        
            
            
            
        
        