class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans, curr = 0, 0
        
        for i in range(len(nums)):
            curr = nums[i]
            if curr == k:
                ans+=1
            for j in range(i+1,len(nums)):
                curr = math.gcd(curr,nums[j])
                if curr == k:
                    ans += 1
                
        return ans
                
                
                
        