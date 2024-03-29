class Solution:
    def numDecodings(self, s: str) -> int:
        # codes = set([str(i) for i in range(1,27)])
        # if len(s) < 2:
        #     return int(s in codes)
        # dp = [0 for _ in range(len(s))]
        # dp[0] = int(s[:1] in codes)
        # dp[1] = int(s[:2] in codes) + (s[0] in codes)*(s[1] in codes)
        # for i in range(2, len(s)):
        #     dp[i] = dp[i - 2]*(s[i - 1 : i + 1] in codes) + dp[i - 1]*(s[i] in codes)
        # return dp[-1]
        dp={}
        def check(idx):
            if idx<len(s) and s[idx]=="0":
                return 0
            if idx>=len(s)-1:
                return 1
            if idx in dp:
                return dp[idx]
            if idx+1< len(s) and int(s[idx]+s[idx+1])<=26:
                dp[idx]=check(idx+1)+check(idx+2)
            else:
                dp[idx]=check(idx+1)
            return dp[idx]
        return check(0)
        
        