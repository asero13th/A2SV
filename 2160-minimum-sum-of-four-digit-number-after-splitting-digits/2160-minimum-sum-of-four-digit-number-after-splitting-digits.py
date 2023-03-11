class Solution:
    def minimumSum(self, num: int) -> int:
        s=list(str(num))
        s.sort()
        ans=int(s[0]+s[2])+int(s[1]+s[3])
        return ans
        