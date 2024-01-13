class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c = Counter(s)
        d = Counter(t)
        
        e = 0
        
        for i in c:
            e += max(0, c[i] - d[i])
        return e