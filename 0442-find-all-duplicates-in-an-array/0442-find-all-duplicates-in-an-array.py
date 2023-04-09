class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        ans = []
        for val in c:
            if c[val] == 2:
                ans.append(val)
        return ans
            