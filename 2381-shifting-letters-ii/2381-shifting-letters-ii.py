class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        words = "abcdefghijklmnopqrstuvwxyz"
        ans = [0] * len(s)
        for left, right, direction in shifts:
            ans[left] += 1 if direction == 1 else -1
            if right != len(s) - 1: ans[right + 1] -= 1 if direction == 1 else -1
        prefix = list(accumulate(ans))
        
        for i, val in enumerate(s):
            s[i] = words[(words.index(val) + prefix[i]) % len(words)]
        return "".join(s)
            