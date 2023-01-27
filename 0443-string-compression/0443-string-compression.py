class Solution:
    def compress(self, chars: List[str]) -> int:
        r, l = 0,0
        s = ""
        if len(chars) == 1:
            return 1
        while r < len(chars):
            tmp = r - l + 1
            if r == len(chars) - 1:
                if tmp > 1:
                    s += chars[r] + str(tmp)
                else:
                    s += chars[r]
            elif chars[r] != chars[r+1]:
                if tmp > 1:
                    s += chars[r] + str(tmp)
                    l = r + 1
                else:
                    s += chars[r]
                    l = r + 1
            r += 1
        chars.clear()
        chars += [i for i in s]
        return len(s)