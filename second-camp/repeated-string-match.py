class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:

        p, i = 0, 1
        lsp = [0] * len(b)
        while i < len(b):
            if b[i] == b[p]:
                lsp[i] = p + 1
                i += 1
                p += 1
            elif p != 0:
                p = lsp[p - 1]
            
            else:
                i += 1
        i, j = 0, 0
        ans  = 0
        while i <= len(a) :
            print(i, j)
            if i == len(a):
                i  = 0
                ans += 1

            if a[i] == b[j]:
                i += 1
                j += 1

            elif j == 0:
                if ans > 1:
                    return -1
                i += 1

            else:
                if ans > 1:
                    return -1
                j = lsp[j - 1]
            
            if j == len(b):
                return ans + 1
        return ans

            
            

        