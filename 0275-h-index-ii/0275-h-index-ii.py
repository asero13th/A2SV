class Solution:
    def hIndex(self, A: List[int]) -> int:
        n = len(A)
        l, r = 0, n - 1
        while l < r:
            m = (l + r + 1) // 2
            if A[m] > n - m: r = m - 1
            else: l = m
        return n - l - (A[l] < n - l)
        