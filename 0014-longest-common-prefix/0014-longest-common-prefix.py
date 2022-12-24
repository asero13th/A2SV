class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        
        for s in strs:
            tmp = ""
            for i in range(min(len(ans),len(s))):
                
                if ans[i] == s[i]:
                    tmp += s[i]
                else:
                    break
            ans = tmp
        return ans
        
        
            
        