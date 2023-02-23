class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        prefix = 0
        ans = 0
        
        for i in range(len(nums)):
            prefix += nums[i]
            division = (prefix % k)
            ans += hashmap.get(division, 0)
            
            hashmap[division] = hashmap.get(division,0) + 1
        return ans