class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        l, r, res, st = 0, len(s)-1, 0, list(s)
        while l < r:
            if st[l] != st[r]:
                i = r
                while i > l and st[l] != st[i]:
                    i -= 1
                if i == l:
                    st[i], st[i+1] = st[i+1], st[i]
                    res += 1
                    continue
                else:
                    while i < r:
                        st[i], st[i+1] = st[i+1], st[i]
                        i += 1
                        res += 1
            l, r = l+1, r-1
        return res
        