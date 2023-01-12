class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        strs = [list(_) for _ in strs]
        ans = 0
        
        zipped = zip(*(strs))
        for _ in zipped:
            if not sorted(_) == list(_):
                ans += 1
        return ans