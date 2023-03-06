class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minstack = []
        for num in nums:
            if not minstack:
                minstack.append(num)
            else:
                minstack.append(min(minstack[-1],num))
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            
                
            while stack  and stack[-1] < nums[i]:
                if minstack[i] < stack[-1]:
                    return True
                stack.pop()
            stack.append(nums[i])
        
        
        
        
        