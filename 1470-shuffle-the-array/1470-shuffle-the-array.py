class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        i = 0
        for i in range(n):
            for j in range(i,len(nums),n):
                ans.append(nums[j])
        return ans
        