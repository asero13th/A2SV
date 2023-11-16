class Solution:
    def minimumRecolors(self, s: str, k: int) -> int:
        min_val = float('inf')
        color_d = {}
        l = 0
        r = 0
        while r < len(s):
            color_d[s[r]] = color_d.get(s[r], 0) + 1
            if r-l+1 == k:
                min_val = min(min_val, color_d['W'] if 'W' in color_d else 0) 
                color_d[s[l]] -=1
                l += 1
            r += 1
        return 0 if min_val == float('inf') else min_val
        