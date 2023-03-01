class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def helper(start, end, turn):
            if start == end:
                return [nums[start], 0] if turn else [0, nums[end]]
            
            if turn:
                ans1 = helper(start + 1, end, not turn)
                ans1[0] += nums[start]
                
                ans2 = helper(start, end - 1, not turn)
                ans2[0] += nums[end]
                
                return ans1 if ans1[0] >= ans2[0] else ans2
                
            else:
                ans1 = helper(start + 1, end, not turn)
                ans1[1] += nums[start]
                
                ans2 = helper(start, end - 1, not turn)
                ans2[1] += nums[end]
                
                return ans1 if ans1[1] >= ans2[1] else ans2
                
        ans = helper(0, len(nums) - 1, True)
        
        return True if ans[0] >= ans[1] else False