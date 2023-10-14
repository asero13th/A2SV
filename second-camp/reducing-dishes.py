class Solution:
    def maxSatisfaction(self, nums: List[int]) -> int:
        nums.sort()

        ans = 0
        print(nums)
        for i in range(len(nums)):
            tmp = 0
            count = 1
            for j in range(i , len(nums)):
                tmp += (nums[j] * count)
                count += 1
            ans = max(ans, tmp)
      
        return ans

        
        
        
            



            





        