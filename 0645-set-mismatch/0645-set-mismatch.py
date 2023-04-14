class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set(nums)
        ans = []
        c = Counter(nums)
        for val in c:
            if c[val] == 2:
                ans.append(val)
        for i in range(1,len(nums) + 1):
            if i not in s:
                ans.append(i)
        return ans
                
        
          
        