class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        strs = [list(_) for _ in strs]
        ans = 0
        print(strs)
        zipped = zip(*(strs))
        for _ in zipped:
            if not sorted(_) == list(_):
                ans += 1
        return ans