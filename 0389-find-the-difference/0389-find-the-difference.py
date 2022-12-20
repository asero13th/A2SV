class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1 = Counter(s)
        t1 = Counter(t)
        for val in t1:
            if val not in s1 or s1[val] != t1[val]:
                return val
                
            