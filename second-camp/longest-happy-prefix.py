class Solution:
    def longestPrefix(self, s: str) -> str:
        p, i = 0, 1
        lsp = [0] * len(s)
        while i < len(s):
            if s[i] == s[p]:
                lsp[i] = p + 1
                i += 1
                p += 1
            elif p != 0:
                p = lsp[p - 1]
            
            else:
                i += 1

        return (s[:lsp[-1]])
        